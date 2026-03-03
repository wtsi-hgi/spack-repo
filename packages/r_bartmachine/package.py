# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBartmachine(RPackage):
	"""Bayesian Additive Regression Trees

	An advanced implementation of Bayesian Additive Regression Trees with expanded features for data analysis and visualization.
	"""
	
	cran = "bartMachine" 

	version("1.3.4.1", md5="24c3e4169fc495cbeb441759872e3abf")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rjava@0.9.8:", type=("build", "run"))
	depends_on("r-bartmachinejars@1.2.1:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
