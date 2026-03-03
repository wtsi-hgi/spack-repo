# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgamma(RPackage):
	"""Generalized Gamma Probability Distribution

	Density, distribution function, quantile function and random generation for the Generalized Gamma proposed in Stacy, E. W. (1962) <doi:10.1214/aoms/1177704481>.
	"""
	
	homepage = "https://mjsaldanha.com/posts/ggamma"
	cran = "ggamma" 

	version("1.0.1", md5="76f5069f74804e187b6efff2252ce03c")

	depends_on("r@3.1:", type=("build", "run"))
