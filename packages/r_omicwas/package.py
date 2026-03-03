# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicwas(RPackage):
	"""Cell-Type-Specific Association Testing in Bulk Omics Experiments

	In bulk epigenome/transcriptome experiments, molecular expression
    is measured in a tissue, which is a mixture of multiple types of cells.
    This package tests association of a disease/phenotype with a molecular marker
    for each cell type.
    The proportion of cell types in each sample needs to be given as input.
    The package is applicable to epigenome-wide association study (EWAS) and
    differential gene expression analysis.
    Takeuchi and Kato (submitted)
    "omicwas: cell-type-specific epigenome-wide and transcriptome association study".
	"""
	
	homepage = "https://github.com/fumi-github/omicwas"
	cran = "omicwas" 

	version("0.8.0", md5="3d110d8db6549d5d6abcfe63445676a0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
