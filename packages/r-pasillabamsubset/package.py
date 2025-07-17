# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPasillabamsubset(RPackage):
    """Subset of BAM files from "Pasilla" experiment

    Subset of BAM files untreated1.bam (single-end reads) and untreated3.bam (paired-end reads) from "Pasilla" experiment (Pasilla knock-down by Brooks et al., Genome Research 2011). See the vignette in the pasilla data package for how BAM files untreated1.bam and untreated3.bam were obtained from the RNA-Seq read sequence data that is provided by NCBI Gene Expression Omnibus under accession numbers GSM461176 to GSM461181.  Also contains the DNA sequence for fly chromosome 4 to which the reads can be mapped.
    """

    bioc = "pasillaBamSubset"

    version("0.46.0", commit="ebf9eafbe63e216f040d4d5ca7cb852496462f0a")
    version("0.40.0", commit="72541462d2ec39b965f5498a9e78eefb272df2d7")
