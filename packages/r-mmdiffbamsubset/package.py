# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmdiffbamsubset(RPackage):
    """Example ChIP-Seq data for the MMDiff package

    Subset of BAM files, including WT_2.bam, Null_2.bam, Resc_2.bam, Input.bam from the "Cfp1" experiment (see Clouaire et al., Genes Dev. 2012). Data is available under ArrayExpress accession numbers E-ERAD-79. Additionally, corresponding subset of peaks called by MACS
    """

    bioc = "MMDiffBamSubset"

    version("1.44.0", commit="e3c56ad24898982d916bfb3dafcc97ba2c87822b")
    version("1.38.0", commit="918a72a36b2f5b7e5099fef96c6338d4262ae16a")
