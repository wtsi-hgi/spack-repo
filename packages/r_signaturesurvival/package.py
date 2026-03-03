# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignaturesurvival(RPackage):
	"""Signature Survival Analysis

	When multiple Cox proportional hazard models are performed on clinical data 
    (month or year and status) and a set of differential expressions of genes, 
    the results (Hazard risks, z-scores and p-values) can be used to create gene-expression signatures. 
    Weights are calculated using the survival p-values of genes and are utilized to calculate expression 
    values of the signature across the selected genes in all patients in a cohort. A Single or multiple 
    univariate or multivariate Cox proportional hazard survival analyses of the patients in one cohort 
    can be performed by using the gene-expression signature and visualized using our survival plots.
	"""
	
	cran = "signatureSurvival" 

	version("1.0.0", md5="b6f7bdcae107821edbc13f232555374e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
