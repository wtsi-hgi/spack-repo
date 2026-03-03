# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbm(RPackage):
	"""Individual Based Models in R

	Implementation of some Individual Based Models (IBMs, sensu Grimm and Railsback 2005) 
  and methods to create new ones, particularly for population dynamics models (reproduction, 
  mortality and movement). The basic operations for the simulations are implemented in Rcpp for speed.
	"""
	
	homepage = "https://roliveros-ramos.github.io/ibm/"
	cran = "ibm" 

	version("0.3.0", md5="63ca51148ebc820dffe5f2dc9f9ec1b4")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
