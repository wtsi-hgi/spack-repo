# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os

from spack.package import *


class Shapeit5(MakefilePackage):
    """SHAPEIT5 estimates haplotypes in large datasets, with a special focus on rare variants."""

    git = "https://github.com/odelaneau/shapeit.git"

    version("5.1.1", commit="f9d726472df3f26120fe738a137fc41cbcc0bbf4")
    version("5.1.0", tag="v5.1.0")
    version("contig", commit="2c9e551c3dc3779fdfaf65943ef2e309f624bd52")

    depends_on("boost@1.74:+iostreams+program_options+serialization")
    depends_on("htslib")
    depends_on("bzip2", type=("build"))
    depends_on("lzma")
    depends_on("zlib", type=("build"))
    depends_on("xz", type=("build"))
    depends_on("curl", type=("build"))
    depends_on("libdeflate")
    depends_on("libpthread-stubs")

    variant("rarephasing", default=False, description="Re-enable Singelton phasing score.")

    patch("rare_phasing.patch", when="+rarephasing")
    patch("math.patch", when="@5.1.0")

    def edit(self, spec, prefix):
        if os.path.exists(".gitmodules"):
            filter_file(
                "\turl = git@github.com:odelaneau/xcftools.git",
                "\turl = https://github.com/odelaneau/xcftools.git",
                ".gitmodules",
                string=True,
            )
            which("git")("submodule", "update", "--init", "--recursive")

        makefile = FileFilter(*(glob.glob("*/makefile")))
        makefile.filter("CXXFLAG=.*", "CXXFLAG=-O3 -mavx2 -mfma -lm")
        makefile.filter("system: HTSSRC=.*", "system: HTSSRC=" + self.spec["htslib"].prefix)
        makefile.filter("system: DYN_LIBS=.*", "system: DYN_LIBS=-lz -lpthread -lbz2 -llzma -lcurl -lcrypto -lm -ldeflate")
        makefile.filter("system: BOOST_INC=.*", "system: BOOST_INC=" + self.spec["boost"].prefix.include)
        makefile.filter("system: BOOST_LIB_IO=.*", "system: BOOST_LIB_IO=" + self.spec["boost"].prefix.lib + "/libboost_iostreams.a")
        makefile.filter("system: BOOST_LIB_PO=.*", "system: BOOST_LIB_PO=" + self.spec["boost"].prefix.lib + "/libboost_program_options.a")
        makefile.filter("system: BOOST_LIB_SE=.*", "system: BOOST_LIB_SE=" + self.spec["boost"].prefix.lib + "/libboost_serialization.a")

    def build(self, spec, prefix):
        make(
            "all",
            "HTSLIB_INC=" + self.spec["htslib"].prefix.include,
            "HTSLIB_LIB=" + self.spec["htslib"].prefix.lib + "/libhts.a",
            "BOOST_INC=" + self.spec["boost"].prefix.include,
            "BOOST_LIB_IO=" + self.spec["boost"].prefix.lib + "/libboost_iostreams.a",
            "BOOST_LIB_PO=" + self.spec["boost"].prefix.lib + "/libboost_program_options.a",
            "BOOST_LIB_SE=" + self.spec["boost"].prefix.lib + "/libboost_serialization.a",
            "DYN_LIBS=-lz -lpthread -lbz2 -llzma -lcurl -lcrypto -lm -ldeflate "
            "-lboost_iostreams -lboost_program_options -lboost_serialization -lhts",
        )

    def install(self, spec, prefix):
        os.mkdir(prefix.usr)
        os.mkdir(prefix.usr.bin)
        for exe in glob.glob("*/bin/*"):
            install(exe, prefix.usr.bin)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            Executable(join_path(self.prefix.usr.bin, "phase_common"))("--help")

    def setup_run_environment(self, env):
        env.append_path("PATH", join_path(self.prefix, "usr", "bin"))
