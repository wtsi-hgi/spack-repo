# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLprelevance(RPackage):
	"""Relevance-Integrated Statistical Inference Engine

	Provide methods to perform customized inference at individual level by taking 
	contextual covariates into account. Three main functions are provided 
	in this package: (i) LASER(): it generates specially-designed artificial relevant 
	samples for a given case; (ii) g2l.proc(): computes customized fdr(z|x); and (iii) 
	rEB.proc(): performs empirical Bayes inference based on LASERs. The details can be 
	found in Mukhopadhyay, S., and Wang, K (2021, <arXiv:2004.09588>). 
	"""
	
	cran = "LPRelevance" 

	version("3.3", md5="70db44895a701333d246989ded0d4314")

	depends_on("r@4.0.3:", type=("build", "run"))
	depends_on("r-bayesgof", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-locfdr", type=("build", "run"))
	depends_on("r-bolstad2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
