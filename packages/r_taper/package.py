# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaper(RPackage):
	"""Flexible Tree Taper Curves Based on Semiparametric Mixed Models

	Implementation of functions for fitting taper curves (a semiparametric 
  linear mixed effects taper model) to diameter measurements along stems. Further 
  functions are provided to estimate the uncertainty around the predicted curves, 
  to calculate timber volume (also by sections) and marginal (e.g., upper) diameters. 
  For cases where tree heights are not measured, methods for estimating
  additional variance in volume predictions resulting from uncertainties in
  tree height models (tariffs) are provided.  The example data include the taper 
  curve parameters for Norway spruce used in the 3rd German NFI fitted to 380 trees 
  and a subset of section-wise diameter measurements of these trees. The functions 
  implemented here are detailed in Kublin, E., Breidenbach, J., Kaendler, G. (2013)
  <doi:10.1007/s10342-013-0715-0>.
	"""
	
	cran = "TapeR" 

	version("0.5.3", md5="63e79f4c99349313d133aabbb32b7d98")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
