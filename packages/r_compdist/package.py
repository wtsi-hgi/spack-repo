# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompdist(RPackage):
	"""Multisection Composite Distributions

	Computes density function, cumulative distribution function, quantile function and random numbers for a multisection composite distribution specified by the user.  Also fits the user specified distribution to a given data set.  More details of the package can be found in the following paper submitted to the R journal Wiegand M and Nadarajah S (2017)  CompDist: Multisection composite distributions.
	"""
	
	cran = "CompDist" 

	version("1.0", md5="25b1e8cd0deb74a3c6332dc0aa2272e8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-fextremes", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
	depends_on("r-pearsonds", type=("build", "run"))
