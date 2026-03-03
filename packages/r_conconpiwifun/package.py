# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConconpiwifun(RPackage):
	"""Optimisation with Continuous Convex Piecewise (Linear and
Quadratic) Functions

	Continuous convex piecewise linear (ccpl) resp. quadratic (ccpq) functions can be implemented with sorted breakpoints and slopes. This includes functions that are ccpl (resp. ccpq) on a convex set (i.e. an interval or a point) and infinite out of the domain. These functions can be very useful for a large class of optimisation problems. Efficient manipulation (such as log(N) insertion) of such data structure is obtained with map standard template library of C++ (that hides balanced trees). This package is a wrapper on such a class based on Rcpp modules. 
	"""
	
	cran = "ConConPiWiFun" 

	version("0.4.6.1", md5="964e99087a2e80f3a00094560ada650c")

	depends_on("r-rcpp", type=("build", "run"))
