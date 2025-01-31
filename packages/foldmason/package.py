# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Foldmason(Package):
    """FoldMason is a software tool for constructing accurate multiple alignments from large sets of protein structures."""

    homepage = "https://github.com/steineggerlab/foldmason"
    url = "https://github.com/steineggerlab/foldmason/releases/download/2-7bd21ed/foldmason-linux-avx2.tar.gz"

    version(
        "2-7bd21ed",
        sha256="23cb607cf6f37d5f29254a7217a1a14255437c589935580c368bc458a8d3bbd0",
        url="https://github.com/steineggerlab/foldmason/releases/download/2-7bd21ed/foldmason-linux-avx2.tar.gz",
    )

    def install(self, spec, prefix):
        # Create required directories
        mkdirp(prefix.bin)

        # Install all executable files to bin directory
        install("bin/foldmason", prefix.bin)

        # Make files executable
        chmod = which("chmod")
        chmod("+x", join_path(prefix.bin, "foldmason"))
