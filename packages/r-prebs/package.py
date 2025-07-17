# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrebs(RPackage):
    """Probe region expression estimation for RNA-seq data for improved microarray comparability

    The prebs package aims at making RNA-sequencing (RNA-seq) data more comparable to microarray data. The comparability is achieved by summarizing sequencing-based expressions of probe regions using a modified version of RMA algorithm. The pipeline takes mapped reads in BAM format as an input and produces either gene expressions or original microarray probe set expressions as an output.
    """

    bioc = "prebs"

    version("1.48.0", commit="a5f346705dafc0194b46341d9eea470945f9622b")
    version("1.42.0", commit="5fc462af89961c3d0932a6ae52930fd0ef9047ce")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-rpa", type=("build", "run"))
    depends_on("r-genomicranges@1.13.3:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
