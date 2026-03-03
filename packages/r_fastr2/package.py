# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastr2(RPackage):
	"""Foundations and Applications of Statistics Using R (2nd Edition)

	Data sets and utilities to accompany the second edition of
    "Foundations and Applications of Statistics: an Introduction
    using R" (R Pruim, published by AMS, 2017), a text covering
    topics from probability and mathematical statistics at an advanced
    undergraduate level.  R is integrated throughout, and access to all
    the R code in the book is provided via the snippet() function.
	"""
	
	homepage = "https://github.com/rpruim/fastR2"
	cran = "fastR2" 

	version("1.2.4", md5="035d0829a8819e96aefdb11fde922a85", url="https://cran.r-project.org/src/contrib/fastR2_1.2.4.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mosaic@1.3:", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
