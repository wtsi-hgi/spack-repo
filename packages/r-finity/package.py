# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinity(RPackage):
	"""Test for Finiteness of Moments in a Distribution

	The purpose of this package is to tests whether a given 
             moment of the distribution of a given sample is finite or not. For 
             heavy-tailed distributions with tail exponent b, only moments of 
             order smaller than b are finite. Tail exponent and heavy-
             tailedness are notoriously difficult to ascertain. But the 
             finiteness of moments (including fractional moments) can be tested 
             directly. This package does that following the test suggested by 
             Trapani (2016) <doi:10.1016/j.jeconom.2015.08.006>.
	"""
	
	cran = "finity" 

	version("0.1.5", md5="b1565b7e24349fe21ac49ac15a881be2")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stabledist@0.7:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
