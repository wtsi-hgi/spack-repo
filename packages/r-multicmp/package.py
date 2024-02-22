# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulticmp(RPackage):
	"""Flexible Modeling of Multivariate Count Data via the
Multivariate Conway-Maxwell-Poisson Distribution

	A toolkit containing statistical analysis models motivated by multivariate forms of the Conway-Maxwell-Poisson (COM-Poisson) distribution for flexible modeling of multivariate count data, especially in the presence of data dispersion. Currently the package only supports bivariate data, via the bivariate COM-Poisson distribution described in Sellers et al. (2016) <doi:10.1016/j.jmva.2016.04.007>. Future development will extend the package to higher-dimensional data.
	"""
	
	homepage = "http://dx.doi.org/10.1016/j.jmva.2016.04.007"
	cran = "multicmp" 

	version("1.1", md5="3de7cee5fb328e5e9c6334d5dcc13a02")

	depends_on("r-numderiv", type=("build", "run"))
