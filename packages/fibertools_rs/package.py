# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class FibertoolsRs(Package):
    """CLI tool for creating and interacting with Fiber-seq BAM files.

    fibertools-rs provides tools for Fiber-seq data written in Rust,
    including capabilities for m6A predictions, nucleosome calling,
    and various data extraction and manipulation functions."""

    homepage = "https://github.com/fiberseq/fibertools-rs"
    url = "https://github.com/fiberseq/fibertools-rs/archive/refs/tags/v0.6.4.tar.gz"

    # License information from the repository
    license("MIT")

    version("0.6.4", sha256="8979d98eff93ccebe85dbc6d40d39d6073fdee10d8cf33d3e37eb5bc145cde05")

    depends_on("rust+dev@1.85:", type="build")
    depends_on("cmake", type="build")

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("build", "--release")
        mkdirp(prefix.bin)
        install("target/release/ft", prefix.bin)
