# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqcovarimpute(RPackage):
	"""Impute Covariate Data in RNA Sequencing Studies

	The RNAseqCovarImpute package implements multiple imputation of missing covariates and differential gene expression analysis by: 1) Randomly binning genes into smaller groups, 2) Creating M imputed datasets separately within each bin, where the imputation predictor matrix includes all covariates and the log counts per million (CPM) for the genes within each bin, 3) Estimating gene expression changes using voom followed by lmFit functions, separately on each M imputed dataset within each gene bin, 4) Un-binning the gene sets and stacking the M sets of model results before applying the squeezeVar function to apply a variance shrinking Bayesian procedure to each M set of model results, 5) Pooling the results with Rubins’ rules to produce combined coefficients, standard errors, and P-values, and 6) Adjusting P-values for multiplicity to account for false discovery rate (FDR).
	"""
	
	homepage = "https://github.com/brennanhilton/RNAseqCovarImpute"
	bioc = "RNAseqCovarImpute" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RNAseqCovarImpute_1.0.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RNAseqCovarImpute/RNAseqCovarImpute_1.0.2.tar.gz"]

	version("1.0.2", md5="17d14273ae359562d3f0cbf1c45b10a7")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
