# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Angsd(MakefilePackage):
    """ANGSD analyses next-generation sequencing data for population genetics."""

    homepage = "http://www.popgen.dk/angsd/index.php/ANGSD"
    url = "https://github.com/ANGSD/angsd/releases/download/0.940/angsd0.940.tar.gz"

    license("UNKNOWN")

    version("0.940", sha256="11c18e8c239b9ffbbfac317008582e63cddeda85f57b8ea4e6fbcae00415dfac")
    version("0.938", sha256="4f0b832cede3237c6925a0338b0cabda365c0e620d630c9d6dad4e2c3a019653")
    version("0.936", sha256="57db1939818f47028002bf172a4f71815b923d19b11f7eb9d621a5c28871e8fb")
    version("0.934", sha256="cb52f7b90698e3a6fa5880984418f9d44073121611d8c3276223fd1e6909bfb2")

    depends_on("htslib", type=("build", "link", "run"))
    depends_on("curl", type=("build", "link", "run"))
    depends_on("zlib", type=("build", "link", "run"))
    depends_on("bzip2", type=("build", "link", "run"))
    depends_on("xz", type=("build", "link", "run"))
    depends_on("openssl", type=("build", "link", "run"))

    build_directory = "angsd"

    build_targets = ["HTSSRC=systemwide"]

    def setup_build_environment(self, env):
        spec = self.spec

        header_deps = ("htslib", "curl", "zlib", "bzip2", "xz", "openssl")
        for dep in header_deps:
            headers = spec[dep].headers
            if headers:
                env.append_flags("CPPFLAGS", headers.include_flags)

        library_deps = ("htslib", "curl", "zlib", "bzip2", "xz", "openssl")
        for dep in library_deps:
            libs = spec[dep].libs
            if libs:
                env.append_flags("LDFLAGS", libs.ld_flags)

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            make("HTSSRC=systemwide", f"prefix={prefix}", "install-all")

    @run_after("install")
    def install_test(self):
        """Exercise the main executable after installing."""
        angsd = Executable(join_path(self.prefix.bin, "angsd"))
        with working_dir("spack-test", create=True):
            angsd("--help")
