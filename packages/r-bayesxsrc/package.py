# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesxsrc(RPackage):
	"""Distribution of the 'BayesX' C++ Sources

	'BayesX' performs Bayesian inference in structured additive regression (STAR) models.
	The R package BayesXsrc provides the 'BayesX' command line tool for easy installation.
	A convenient R interface is provided in package R2BayesX.
	"""
	
	homepage = "https://www.uni-goettingen.de/de/bayesx/550513.html"
	cran = "BayesXsrc" 

	version("3.0-5", md5="d0c7960aa875fcf8f5a3ac8e852c52b0")
	version("3.0-4", md5="5c989dc84940a26b85c5c24dd21a05c1")

	depends_on("r@2.8:", type=("build", "run"))
