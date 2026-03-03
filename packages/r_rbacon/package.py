# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbacon(RPackage):
	"""Age-Depth Modelling using Bayesian Statistics

	An approach to age-depth modelling that uses Bayesian statistics to reconstruct accumulation histories for deposits, through combining radiocarbon and other dates with prior information on accumulation rates and their variability. See Blaauw & Christen (2011).
	"""
	
	cran = "rbacon" 

	version("3.2.0", md5="83c94286ceb4758085bfcb8c18b9e8af")

	depends_on("r-rintcal@0.6.4:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda@0.19.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
