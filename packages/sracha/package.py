# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Sracha(Package):
    """Fast SRA downloader and FASTQ converter implemented in Rust."""

    maintainers("softpack-bot")

    homepage = "https://github.com/rnabioco/sracha-rs"
    url = "https://github.com/rnabioco/sracha-rs/archive/refs/tags/v0.1.9.tar.gz"

    license("MIT")

    version("0.1.9", sha256="60e21d25c810b53358bf2be8e9964822b186162e82b48b964523af6fee3ec307")

    depends_on("rust@1.92:", type="build")
    depends_on("cmake", type="build")

    def install(self, spec, prefix):
        cargo = Executable(join_path(spec["rust"].prefix.bin, "cargo"))
        cargo("install", "--locked", "--root", prefix, "--path", "crates/sracha")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            Executable(join_path(self.prefix.bin, "sracha"))("--help")
