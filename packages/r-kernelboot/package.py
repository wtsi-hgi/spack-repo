# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKernelboot(RPackage):
	"""Smoothed Bootstrap and Random Generation from Kernel Densities

	Smoothed bootstrap and functions for random generation from
             univariate and multivariate kernel densities. It does not
             estimate kernel densities.
	"""
	
	homepage = "https://github.com/twolodzko/kernelboot"
	cran = "kernelboot" 

	version("0.1.10", md5="b491e53ad345159ec09eca3322b87dde")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
