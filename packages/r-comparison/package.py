# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparison(RPackage):
	"""Multivariate Likelihood Ratio Calculation and Evaluation

	Functions for calculating and evaluating likelihood ratios from uni/multivariate continuous observations.
	"""
	
	homepage = "https://github.com/jmcurran/comparison"
	cran = "comparison" 

	version("1.0.8", md5="a578bd9032300fb9419723c9dbe416d9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-isotone", type=("build", "run"))
	depends_on("r-cvglasso", type=("build", "run"))
