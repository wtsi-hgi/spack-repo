# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimization(RPackage):
	"""Flexible Optimization of Complex Loss Functions with State and
Parameter Space Constraints

	Flexible optimizer with numerous input specifications for detailed
  parameterisation. Designed for complex loss functions with state and 
  parameter space constraints. Visualization tools for validation and analysis
  of the convergence are included.
	"""
	
	homepage = "https://github.com/kaihusmann/optimization"
	cran = "optimization" 

	version("1.0-9", md5="720b929f5ba549895c242ed4d57c4daf")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
