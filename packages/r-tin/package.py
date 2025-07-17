# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTin(RPackage):
    """Transcriptome instability analysis

    The TIN package implements a set of tools for transcriptome instability analysis based on exon expression profiles. Deviating exon usage is studied in the context of splicing factors to analyse to what degree transcriptome instability is correlated to splicing factor expression. In the transcriptome instability correlation analysis, the data is compared to both random permutations of alternative splicing scores and expression of random gene sets.
    """

    bioc = "TIN"

    version("1.40.0", commit="d31829d20d61582f9ef6c2f0ebae9eefdb245313")
    version("1.34.0", commit="d6f3adfb8bf178049f1d2c5bcc9c9cb7ab8601cf")

    depends_on("r@2.12:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-impute", type=("build", "run"))
    depends_on("r-aroma-affymetrix", type=("build", "run"))
    depends_on("r-wgcna", type=("build", "run"))
    depends_on("r-squash", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
