# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdge(RPackage):
    """Extraction of Differential Gene Expression

    The edge package implements methods for carrying out differential expression analyses of genome-wide gene expression studies. Significance testing using the optimal discovery procedure and generalized likelihood ratio tests (equivalent to F-tests and t-tests) are implemented for general study designs. Special functions are available to facilitate the analysis of common study designs, including time course experiments. Other packages such as snm, sva, and qvalue are integrated in edge to provide a wide range of tools for gene expression analysis.
    """

    homepage = "https://github.com/jdstorey/edge"
    bioc = "edge"

    version("2.40.0", commit="8281a3b167a754869bc4027d71bb86400b2722e7")
    version("2.34.0", commit="07c69be24cff5b3da15bf194fd4e3544b26df2d4")

    depends_on("r@3.1:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-sva", type=("build", "run"))
    depends_on("r-snm", type=("build", "run"))
    depends_on("r-qvalue@1.99:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
