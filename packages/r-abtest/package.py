# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbtest(RPackage):
	"""Bayesian A/B Testing

	Provides functions for Bayesian A/B testing including prior elicitation
    options based on Kass and Vaidyanathan (1992) <doi:10.1111/j.2517-6161.1992.tb01868.x>. 
    Gronau, Raj K. N., & Wagenmakers (2021) <doi:10.18637/jss.v100.i17>.
	"""
	
	cran = "abtest" 

	version("1.0.1", md5="50168fec5da503d80fadff307e4bdf6e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-qgam", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
