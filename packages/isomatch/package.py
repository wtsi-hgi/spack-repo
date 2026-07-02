# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Isomatch(Package):
    """Accurate and scalable transcript merging and classification for
    long- and short-read RNA-seq transcript models."""

    homepage = "https://github.com/zhengxinchang/isomatch"
    url = "https://github.com/zhengxinchang/isomatch/archive/refs/tags/v0.6.0.tar.gz"

    license("MIT")

    version("0.6.0", sha256="a78314fda832f0684be193c7009ef47c38115d38d4985d6b1e6b9a29e30d63f0")

    depends_on("rust@1.92:", type="build")

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("install", "--locked", "--root", prefix, "--path", ".")

    @run_after("install")
    def install_test(self):
        """Basic CLI smoke test to confirm the binary executes."""
        with working_dir("spack-test", create=True):
            Executable(self.prefix.bin.isomatch)("--help")
