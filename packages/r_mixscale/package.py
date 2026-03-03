# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RMixscale(RPackage):
    """Mixscale is an R package designed to analyze CRISPR interference (CRISPRi) based Perturb-seq data. It can quantify the heterogeneity of perturbation strength in each cell and improve the statistical power when doing differential expression (DE) analysis. It also provides functions for downstream analyses including decomposition, permutation test, gene set enrichment test, etc."""

    homepage = "https://github.com/longmanz/Mixscale"
    git = "https://github.com/longmanz/Mixscale.git"

    version("2024-04-22", commit="94766c7f415702bcde011745c23270e757435752")

    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-seuratobject", type=("build", "run"))
    depends_on("r-glmgampoi", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggridges", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-pma", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-protoclust", type=("build", "run"))
