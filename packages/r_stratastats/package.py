# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratastats(RPackage):
	"""Stratified Analysis of 2x2 Contingency Tables

	Offers a comprehensive approach for analysing stratified 2x2 contingency tables. It facilitates the calculation of odds ratios, 95% confidence intervals, and conducts chi-squared, Cochran-Mantel-Haenszel, Mantel-Haenszel, and Breslow-Day-Tarone tests. The package is particularly useful in fields like epidemiology and social sciences where stratified analysis is essential. The package also provides interpretative insights into the results, aiding in the understanding of statistical outcomes.
	"""
	
	cran = "stratastats" 

	version("0.2", md5="1680204abc8a17f625bbdf73056da503")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-abind@1.4:", type=("build", "run"))
	depends_on("r-gt@0.8:", type=("build", "run"))
