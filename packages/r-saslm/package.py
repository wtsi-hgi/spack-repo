# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaslm(RPackage):
	"""'SAS' Linear Model

	This is a core implementation of 'SAS' procedures for linear models - GLM, REG, ANOVA, TTEST, FREQ, and UNIVARIATE. Some R packages provide type II and type III SS. However, the results of nested and complex designs are often different from those of 'SAS.' Different results does not necessarily mean incorrectness. However, many wants the same results to SAS. This package aims to achieve that. 
             Reference: Littell RC, Stroup WW, Freund RJ (2002, ISBN:0-471-22174-0).
	"""
	
	homepage = "https://cran.r-project.org/package=sasLM"
	cran = "sasLM" 

	version("0.10.2", md5="13cf01ea4ab1d6f724d0c1a4b6f5edb5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
