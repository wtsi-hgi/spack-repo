# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvidencefactors(RPackage):
	"""Reporting Tools for Sensitivity Analysis of Evidence Factors in
Observational Studies

	Provides tools for integrated sensitivity analysis of evidence factors in observational
	studies. When an observational study allows for multiple independent or nearly
	independent inferences which, if vulnerable, are vulnerable to different biases, we have 
	multiple evidence factors.  This package provides methods that respect type I error rate control. 
	Examples are provided of integrated evidence factors analysis in a longitudinal study with
	continuous outcome and in a case-control study. 
	Karmakar, B., French, B., and Small, D. S. (2019)<DOI:10.1093/biomet/asz003>.
	"""
	
	cran = "evidenceFactors" 

	version("1.8", md5="6e1ab5162b2b8e0bd7bfa7958d4cb7f8")

	depends_on("r-sensitivitymv", type=("build", "run"))
