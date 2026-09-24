# Copyright 2013-2026 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Quasar(CMakePackage):
    """Efficient and versatile software for expression quantitative trait
    loci (eQTL) mapping."""

    homepage = "https://jeffreypullin.github.io/quasar/"
    url = "https://github.com/jeffreypullin/quasar/archive/refs/tags/1.2.1.tar.gz"
    git = "https://github.com/jeffreypullin/quasar.git"

    license("GPL-3.0-only")

    version("1.2.1", sha256="66d13082b65cb589dd0cba7d703aa86c16d6601a3a9ea764abf1649b51be7174")
    version("1.2.0", sha256="f0a046f0e318f0494d8b7e5cb66a692f2b776e9c08f5970174e6e310c18f4482")
    version("1.1.0", sha256="46fc4a8ba418667755740eda6913166652ba01d1ec4312c3018226e20f26865a")
    version("1.0.0", sha256="67f56fb41a287fa98f40673ac1517adf8f9f6ce0a5a9cf3ca209ec53f86f9552")

    depends_on("cmake@3.13:", type="build")
    depends_on("boost")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path(self.build_directory, "quasar"), prefix.bin)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            Executable(join_path(self.prefix.bin, "quasar"))("--version")
