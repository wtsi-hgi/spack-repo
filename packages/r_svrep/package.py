# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvrep(RPackage):
	"""Tools for Creating, Updating, and Analyzing Survey Replicate
Weights

	Provides tools for creating and working with survey replicate weights,
  extending functionality of the 'survey' package from Lumley (2004) <doi:10.18637/jss.v009.i08>.
  Implements bootstrap methods for complex surveys, including the generalized survey bootstrap
  as described by Beaumont and Patak (2012) <doi:10.1111/j.1751-5823.2011.00166.x>.
  Methods are provided for applying nonresponse adjustments to
  both full-sample and replicate weights as described by 
  Rust and Rao (1996) <doi:10.1177/096228029600500305>.
  Implements methods for sample-based calibration described by Opsomer and Erciulescu (2021) 
  <https://www150.statcan.gc.ca/n1/pub/12-001-x/2021002/article/00006-eng.htm>.
  Diagnostic functions are included to compare weights and weighted estimates
  from different sets of replicate weights.
	"""
	
	homepage = "https://bschneidr.github.io/svrep/"
	cran = "svrep" 

	version("0.6.3", md5="f8293e7dfee37edd569a21885cd0a8b6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survey@4.1:", type=("build", "run"))
