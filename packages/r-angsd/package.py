# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAngsd(MakefilePackage):
    """ANGSD (Analysis of Next Generation Sequencing Data) calculates a wide
    range of population genetics statistics directly from sequencing data."""

    homepage = "https://github.com/ANGSD/angsd"
    url = "https://github.com/ANGSD/angsd/archive/refs/tags/0.941.tar.gz"
    git = "https://github.com/ANGSD/angsd.git"

    version("0.941", sha256="760ba3066d7cb24e9eea5c85fd67a611d3edf8b9509295efc48d689c1808a026")

    depends_on("htslib")
    depends_on("zlib")
    depends_on("bzip2")
    depends_on("xz")
    depends_on("curl")
    depends_on("openssl")

    def setup_build_environment(self, env):
        env.append_flags("CPPFLAGS", f"-I{self.spec['htslib'].prefix.include}")
        env.append_flags("LDFLAGS", self.spec["htslib"].libs.search_flags)

    def build(self, spec, prefix):
        make("HTSSRC=systemwide")

    def install(self, spec, prefix):
        make("HTSSRC=systemwide", f"prefix={prefix}", "install")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            Executable(join_path(self.prefix.bin, "angsd"))("--help")
