# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Libwfa(CMakePackage):
    """Wave-function analysis toolkit used by multiple quantum chemistry codes."""

    homepage = "https://libwfa.github.io/libwfa"
    git = "https://github.com/libwfa/libwfa.git"

    license("BSD-3-Clause")

    version("20241007", commit="261d88f5a0d7bdf24ec09a426f0b45b97caf909a")

    variant("molcas_lib", default=False, description="Build the Molcas interface library")
    variant("molcas_exe", default=False, description="Build the standalone Molcas executable")
    variant("arma_header", default=False, description="Include Armadillo headers directly")

    conflicts(
        "+molcas_lib",
        when="+molcas_exe",
        msg="Molcas executable mode is only available for standalone builds.",
    )

    depends_on("cmake@3.16:", type="build")
    depends_on("armadillo@3.6.2:")

    depends_on("hdf5+cxx", when="+molcas_lib")
    depends_on("hdf5+cxx", when="+molcas_exe")
    depends_on("blas", when="+molcas_exe")
    depends_on("lapack", when="+molcas_exe")

    def cmake_args(self):
        return [
            self.define_from_variant("MOLCAS_LIB", "molcas_lib"),
            self.define_from_variant("MOLCAS_EXE", "molcas_exe"),
            self.define_from_variant("ARMA_HEADER", "arma_header"),
        ]

    def install(self, spec, prefix):
        lib_dir = join_path(self.build_directory, "libwfa")
        lib_targets = ["libwfa.a", "libwfa_molcas.a"]
        mkdirp(prefix.lib)
        copied_lib = False
        for lib_name in lib_targets:
            candidate = join_path(lib_dir, lib_name)
            if os.path.isfile(candidate):
                install(candidate, join_path(prefix.lib, lib_name))
                copied_lib = True

        if "+molcas_exe" in spec:
            molcas_exe = join_path(self.build_directory, "libwfa", "molcas", "wfa_molcas.x")
            if os.path.isfile(molcas_exe):
                mkdirp(prefix.bin)
                install(molcas_exe, prefix.bin)

        include_src = join_path(self.stage.source_path, "libwfa")
        include_dst = join_path(prefix.include, "libwfa")
        header_exts = (".h", ".hpp", ".hh")
        for dirpath, _, filenames in os.walk(include_src):
            headers = [f for f in filenames if f.lower().endswith(header_exts)]
            if not headers:
                continue
            rel = os.path.relpath(dirpath, include_src)
            dest_dir = include_dst if rel == "." else join_path(include_dst, rel)
            mkdirp(dest_dir)
            for header in headers:
                install(join_path(dirpath, header), dest_dir)

        if not copied_lib:
            raise InstallError("No libwfa library artifacts were produced during the build.")

    @run_after("install")
    def install_test(self):
        """Build and run a tiny program that links against libwfa."""
        libs = find_libraries("libwfa", root=self.prefix, shared=False, recursive=True)
        if not libs:
            libs = find_libraries("libwfa_molcas", root=self.prefix, shared=False, recursive=True)
        if not libs:
            raise InstallError("Unable to locate installed libwfa libraries for testing.")

        libs += self.spec["armadillo"].libs
        extra_libs = []
        if "+molcas_lib" in self.spec or "+molcas_exe" in self.spec:
            extra_libs.append(self.spec["hdf5"].libs)
        if "+molcas_exe" in self.spec:
            extra_libs.extend([self.spec["blas"].libs, self.spec["lapack"].libs])
        for ll in extra_libs:
            libs += ll

        test_source = """\
#include <libwfa/version.h>
#include <string>

int main() {
    const auto version = libwfa::version::get_string();
    const auto license = libwfa::version::get_license();
    if (version.empty() || license.empty()) {
        return 1;
    }
    return static_cast<int>(libwfa::version::get_major() == 0);
}
"""
        cxx = Executable(self.compiler.cxx)

        with working_dir("spack-test", create=True):
            source = "libwfa_test.cpp"
            with open(source, "w", encoding="utf-8") as f:
                f.write(test_source)

            cxx(
                source,
                "-std=c++11",
                "-I{0}".format(join_path(self.prefix, "include")),
                "-L{0}".format(join_path(self.prefix, "lib")),
                *libs.ld_flags.split(),
                "-o",
                "libwfa-test",
            )

            Executable("./libwfa-test")()
