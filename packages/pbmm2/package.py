# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Pbmm2(Package):
    """A minimap2 SMRT wrapper for PacBio data: native PacBio data in ⇨ native PacBio BAM out.

    pbmm2 is a SMRT C++ wrapper for minimap2's C API. Its purpose is to support native PacBio
    in- and output, provide sets of recommended parameters, generate sorted output on-the-fly,
    and postprocess alignments. Sorted output can be used directly for polishing using GenomicConsensus,
    if BAM has been used as input to pbmm2. Benchmarks show that pbmm2 outperforms BLASR in
    sequence identity, number of mapped bases, and especially runtime. pbmm2 is the official
    replacement for BLASR.
    """

    homepage = "https://github.com/PacificBiosciences/pbmm2"

    license("BSD-3-Clause-Clear")

    version("1.17.0", url="https://github.com/PacificBiosciences/pbmm2/releases/download/v1.17.0/pbmm2", sha256="26c8900acd0cc105de53429aaff69d71ae2c8d222ec147e54097db3f5c927ba8", expand=False)
    version("1.13.1", url="https://github.com/PacificBiosciences/pbmm2/releases/download/v1.13.1/pbmm2", sha256="4e764bbea99a4c712fb74e4d6c82c227562d431c47670628f1d004b2f0e8a8db", expand=False)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/pbmm2", prefix.bin.pbmm2)
        which("chmod")("+x", prefix.bin.pbmm2)
