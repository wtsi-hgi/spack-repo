# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcurver(RPackage):
	"""Utility Functions for Davidian Curves

	A Davidian curve defines a seminonparametric density, whose shape and flexibility can be tuned by
  easy to estimate parameters. Since a special case of a Davidian curve is the standard normal density,
  Davidian curves can be used for relaxing normality assumption in statistical applications (Zhang & Davidian, 2001)
  <doi:10.1111/j.0006-341X.2001.00795.x>. This package provides the density function, the gradient of
  the loglikelihood and a random generator for Davidian curves.
	"""
	
	homepage = "https://github.com/oguzhanogreden/dcurver"
	cran = "dcurver" 

	version("0.9.2", md5="3398f1d3189b8ce16d00beec94e56336")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
