# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaRnaseq(RPackage):
    """Rna-seq datasets from The Cancer Genome Atlas Project

    Package provides rna-seq datasets from The Cancer Genome Atlas Project for all cohorts types from http://gdac.broadinstitute.org/. Rna-seq data format is explained here https://wiki.nci.nih.gov/display/TCGA/RNASeq+Version+2. Data source is illumina hiseq Level 3 RSEM normalized expression data. Data from 2015-11-01 snapshot.
    """

    bioc = "RTCGA.rnaseq"

    version("20151101.38.0", commit="0d4b3eea7deb9ffae88db3346f9784a824b2a979")
    version("20151101.32.0", commit="1f62f3c27d64ead2504dc8c6a7af03f08942252f")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-rtcga", type=("build", "run"))
