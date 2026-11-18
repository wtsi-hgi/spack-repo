# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Fclones(Package):
    """Efficient duplicate file finder and remover."""

    maintainers("softpack-bot")

    homepage = "https://github.com/pkolaczk/fclones"
    url = "https://github.com/pkolaczk/fclones/archive/refs/tags/v0.35.0.tar.gz"

    license("MIT")

    version("0.35.0", sha256="9d8bb36076190f799f01470f80e64c6a1f15f0d938793f8f607a2544cdd6115a")

    depends_on("rust@1.74:", type="build")

    def install(self, spec, prefix):
        cargo = Executable(join_path(spec["rust"].prefix.bin, "cargo"))
        cargo("install", "--locked", "--root", prefix, "--path", "fclones")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            fclones = Executable(join_path(self.prefix.bin, "fclones"))
            fclones("--help")
