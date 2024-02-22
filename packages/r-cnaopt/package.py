# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnaopt(RPackage):
	"""Optimizing Consistency and Coverage in Configurational Causal
Modeling

	This is an add-on to the 'cna' package <https://CRAN.R-project.org/package=cna> comprising various functions for optimizing consistency and coverage scores of models of configurational comparative methods as Coincidence Analysis (CNA) and Qualitative Comparative Analysis (QCA). The function conCovOpt() calculates con-cov optima, selectMax() selects con-cov maxima among the con-cov optima, DNFbuild() can be used to build models actually reaching those optima, and findOutcomes() identifies those factor values in analyzed data that can be modeled as outcomes. For a theoretical introduction to these functions see Baumgartner and Ambuehl (2021) <doi:10.1177/0049124121995554>.
	"""
	
	cran = "cnaOpt" 

	version("0.5.2", md5="cbedf9d01ed3cee9f1b880ac51646399")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cna@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
