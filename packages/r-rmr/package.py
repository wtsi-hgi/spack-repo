# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmr(RPackage):
	"""Importing Data from Loligo Systems Software, Calculating
Metabolic Rates and Critical Tensions

	Analysis of oxygen consumption data generated by Loligo (R) Systems respirometry equipment. The package includes a function for loading data output by Loligo's 'AutoResp' software (get.witrox.data()), functions for calculating metabolic rates over user-specified time intervals, extracting critical points from data using broken stick regressions based on Yeager and Ultsch (<DOI:10.1086/physzool.62.4.30157935>), and easy functions for converting between different units of barometric pressure.
	"""
	
	cran = "rMR" 

	version("1.1.0", md5="42b7825587c973114ba9bd3821391626")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biglm", type=("build", "run"))
