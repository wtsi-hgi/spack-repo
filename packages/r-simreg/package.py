# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimreg(RPackage):
	"""Similarity Regression

	Similarity regression,
    evaluating the probability of association between sets of ontological terms
    and binary response vector. A no-association model is compared with one in which
    the log odds of a true response is linked to the semantic similarity
    between terms and a latent characteristic ontological profile - 'Phenotype Similarity Regression for Identifying the Genetic Determinants of Rare Diseases', Greene et al 2016 <doi:10.1016/j.ajhg.2016.01.008>. 
	"""
	
	cran = "SimReg" 

	version("3.4", md5="9961bd2f57f5f9b7b316233563fd6a7b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ontologyindex@2:", type=("build", "run"))
	depends_on("r-ontologysimilarity@2:", type=("build", "run"))
	depends_on("r-ontologyplot", type=("build", "run"))
