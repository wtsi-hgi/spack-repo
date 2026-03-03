# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTruncatednormal(RPackage):
	"""Truncated Multivariate Normal and Student Distributions

	A collection of functions to deal with the truncated univariate and multivariate normal and Student distributions, described in Botev (2017) <doi:10.1111/rssb.12162> and Botev and L'Ecuyer (2015) <doi:10.1109/WSC.2015.7408180>.
	"""
	
	cran = "TruncatedNormal" 

	version("2.2.2", md5="a4a7e180dfbbfb2aa6f00486667281b9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
