# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarzic(RPackage):
	"""Marginal Mediation Effects with Zero-Inflated Compositional
Mediator

	A way to estimate and test marginal mediation effects for 
             zero-inflated compositional mediators. Estimates of Natural Indirect Effect (NIE),
             Natural Direct Effect (NDE) of each taxon, as well as their standard errors and 
             confident intervals, were provided as outputs. Zeros will not be imputed during 
             analysis. See Wu et al. (2022) <doi:10.3390/genes13061049>. 
	"""
	
	homepage = "https://www.mdpi.com/2073-4425/13/6/1049"
	cran = "MarZIC" 

	version("1.0.0", md5="98434b4184985ccd4c4a98edcd83019d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nlcoptim", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-dirmult", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
