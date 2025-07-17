# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprvariants(RPackage):
    """Tools for counting and visualising mutations in a target location

    CrispRVariants provides tools for analysing the results of a CRISPR-Cas9 mutagenesis sequencing experiment, or other sequencing experiments where variants within a given region are of interest. These tools allow users to localize variant allele combinations with respect to any genomic location (e.g. the Cas9 cut site), plot allele combinations and calculate mutation rates with flexible filtering of unrelated variants.
    """

    bioc = "CrispRVariants"

    version("1.36.0", commit="f45817dcb6140fbb440fa4f043f0ecc2a77d3b10")
    version("1.30.0", commit="871c97928733b7676c0c285db0fe07abc18e1cb0")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-ggplot2@2.2:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-s4vectors@0.9.38:", type=("build", "run"))
