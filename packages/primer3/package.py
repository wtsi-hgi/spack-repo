# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Primer3(Package):
    """Design PCR primers from DNA sequence. Widely used (190k Google hits for "primer3"). From mispriming libraries to sequence quality data to the generation of internal oligos, primer3 does it."""

    homepage = "https://primer3.org"
    url = "https://github.com/primer3-org/primer3/archive/refs/tags/v2.6.1.tar.gz"

    version("2.6.1", sha256="805cef7ef39607cd40f0f5bb8b32e35e20007153a0a55131dd430ce644c8fb9e")
    version("2.6.0", sha256="664903d528cc5473fc55355f6c47da3141b91c0284cf5cc8d219efede2d9a8e3")
    version("2.5.0", sha256="7581e2fa3228ef0ee1ffa427b2aa0a18fc635d561208327471daf59d1b804da0")

    # depends_on("foo")

    def install(self, spec, prefix):
        cd("src")
        make("all")

        mkdir(prefix.bin)

        for file in ["amplicon3_core", "long_seq_tm_test", "ntdpal", "ntthal", "oligotm", "primer3_core", "primer3_masker"]:
            install(file, prefix.bin)
