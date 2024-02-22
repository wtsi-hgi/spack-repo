# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevengc(RPackage):
	"""Reverse Engineering Summarized Data

	Decoupled (e.g. separate averages) and censored (e.g. > 100 species) variables are continually reported by many well-established organizations (e.g. World Health Organization (WHO), Centers for Disease Control and Prevention (CDC), World Bank, and various national censuses).  The challenge therefore is to infer what the original data could have been given summarized information.  We present an R package that reverse engineers decoupled and/or censored count data with two main functions.  The cnbinom.pars function estimates the average and dispersion parameter of a censored univariate frequency table.  The rec function reverse engineers summarized data into an uncensored bivariate table of probabilities.
	"""
	
	homepage = "https://github.com/GIST-ORNL/revengc"
	cran = "revengc" 

	version("1.0.4", md5="ac96a060377ae75c03ea43609b002a2a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mipfp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
