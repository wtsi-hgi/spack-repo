# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeismicroll(RPackage):
	"""Fast Rolling Functions for Seismology using 'Rcpp'

	Fast versions of seismic analysis functions that 'roll' over a
    vector of values. See the 'RcppRoll' package for alternative
    versions of basic statistical functions such as rolling mean,
    median, etc.
	"""
	
	cran = "seismicRoll" 

	version("1.1.5", md5="9d3627796fc85faedd1630900a4c13b8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
