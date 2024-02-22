# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmm(RPackage):
	"""Linear Mixed Models

	It implements Expectation/Conditional Maximization Either (ECME)
             and rapidly converging algorithms as well as
             Bayesian inference for linear mixed models, 
             which is described in Schafer, J.L. (1998)
             "Some improved procedures for linear mixed models".
             Dept. of Statistics, The Pennsylvania State University.
	"""
	
	homepage = "https://github.com/jinghuazhao/R"
	cran = "lmm" 

	version("1.4", md5="e6204b9bf1bcd331bd93131c4d4c4a9e")

	depends_on("r@2:", type=("build", "run"))
