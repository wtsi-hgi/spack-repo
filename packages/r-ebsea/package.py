# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbsea(RPackage):
    """Exon Based Strategy for Expression Analysis of genes

    Calculates differential expression of genes based on exon counts of genes obtained from RNA-seq sequencing data.
    """

    bioc = "EBSEA"

    version("1.36.0", commit="f86728394a13cb70879a84f255566a3636370cb8")
    version("1.30.0", commit="3f6476a6b87cbae1a78bebe043cd3e1e435da2de")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-empiricalbrownsmethod", type=("build", "run"))
