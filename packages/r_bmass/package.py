# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmass(RPackage):
	"""Bayesian Multivariate Analysis of Summary Statistics

	Multivariate tool for analyzing genome-wide association
    study results in the form of univariate summary statistics. The 
    goal of 'bmass' is to comprehensively test all possible multivariate
    models given the phenotypes and datasets provided. Multivariate
    models are determined by assigning each phenotype to being either
    Unassociated (U), Directly associated (D) or Indirectly associated
    (I) with the genetic variant of interest. Test results for each model 
    are presented in the form of Bayes factors, thereby allowing direct
    comparisons between models. The underlying framework implemented
    here is based on the modeling developed in "A Unified Framework 
    for Association Analysis with Multiple Related Phenotypes",
    M. Stephens (2013) <doi:10.1371/journal.pone.0065245>.
	"""
	
	homepage = "https://github.com/mturchin20/bmass"
	cran = "bmass" 

	version("1.0.3", md5="05aadb2f93aff976a8ff2855d9949a5f")

	depends_on("r@3.3:", type=("build", "run"))
