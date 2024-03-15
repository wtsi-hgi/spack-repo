# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigsimr(RPackage):
	"""Fast Generation of High-Dimensional Random Vectors

	Simulate multivariate data with arbitrary marginal distributions.
  'bigsimr' is a package for simulating high-dimensional multivariate data with 
  a target correlation and arbitrary marginal distributions via Gaussian copula. 
  It utilizes the Julia package 'Bigsimr.jl' for its core routines.
	"""
	
	homepage = "https://github.com/SchisslerGroup/r-bigsimr"
	cran = "bigsimr" 

	version("0.12.0", md5="55e85c1cded660566769f611bd7a6ca9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-juliacall", type=("build", "run"))
	depends_on("julia", type=("build", "link", "run"))
