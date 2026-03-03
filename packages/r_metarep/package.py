# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetarep(RPackage):
	"""Replicability-Analysis Tools for Meta-Analysis

	User-friendly package for reporting replicability-analysis methods, affixed to meta-analyses summary. The replicability-analysis output provides an assessment of the investigated intervention, where it offers quantification of effect replicability and assessment of the consistency of findings.
 - Replicability-analysis for fixed-effects and random-effect meta analysis: 
 - r(u)-value;
 - lower bounds on the number of studies with replicated positive andor negative effect;
 - Allows detecting inconsistency of signals;
 - forest plots with the summary of replicability analysis results;
 - Allows Replicability-analysis with or without the common-effect assumption. 
	"""
	
	homepage = "https://github.com/IJaljuli/metarep"
	cran = "metarep" 

	version("1.2.0", md5="2ae0c2279e165fb54c6a478b8e744f5c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-meta@6.0.0:", type=("build", "run"))
