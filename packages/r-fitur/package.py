# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitur(RPackage):
	"""Fit Univariate Distributions

	Wrapper for computing parameters for univariate distributions using MLE. It creates an object that stores d, p, q, r functions as well as parameters and statistics for diagnostics. Currently supports automated fitting from base and actuar packages. A manually fitting distribution fitting function is included to support directly specifying parameters for any distribution from ancillary packages.
	"""
	
	homepage = "https://github.com/tomroh/fitur"
	cran = "fitur" 

	version("0.6.2", md5="36265e308103367efbb59b0ff0df0636")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-goftest", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.5:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
