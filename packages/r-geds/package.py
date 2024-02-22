# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeds(RPackage):
	"""Geometrically Designed Spline Regression

	Geometrically Designed Spline ('GeDS') Regression is a non-parametric geometrically 
  motivated method for fitting variable knots spline predictor models in one or two independent 
  variables, in the context of generalized (non-)linear models. 'GeDS' estimates the number and 
  position of the knots and the order of the spline, assuming the response variable has a 
  distribution from the exponential family. A description of the method can be found in
  Kaishev et al. (2016) <doi:10.1007/s00180-015-0621-7> and Dimitrova et al. (2017) <https://openaccess.city.ac.uk/id/eprint/18460/>.
	"""
	
	homepage = "https://github.com/emilioluissaenzguillen/GeDS"
	cran = "GeDS" 

	version("0.1.4", md5="80b509c311dd3354c8a067fa92a830c6")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
