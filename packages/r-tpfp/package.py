# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpfp(RPackage):
	"""Counts the Number of True Positives and False Positives

	Calculates the number of true positives and false positives from a dataset formatted for Jackknife alternative free-response receiver operating characteristic which is used for statistical analysis which is explained in the book 'Chakraborty' 'DP' (2017), "Observer Performance Methods for Diagnostic Imaging - Foundations, Modeling, and Applications with R-Based Examples", Taylor-Francis <https://www.crcpress.com/9781482214840>.
	"""
	
	cran = "tpfp" 

	version("0.0.1", md5="2a11e08c591569b492272c2453d8ee58")

	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
