# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginDccv(RPackage):
	"""R Commander Plug-in for Dichotomous Choice Contingent Valuation

	Adds menu items to the R Commander for parametric analysis of dichotomous choice contingent valuation (DCCV) data. CV is a question-based survey method to elicit individuals' preferences for goods and services. This package depends on functions regarding parametric DCCV analysis in the package DCchoice. See Carson and Hanemann (2005) <doi:10.1016/S1574-0099(05)02017-6> for DCCV.
	"""
	
	cran = "RcmdrPlugin.DCCV" 

	version("0.1-4", md5="45e83ff99a48b14b0ff56f6be6dce288")
	version("0.1-3", md5="57a205098450facac1455d749ecaeb93")

	depends_on("r-dcchoice", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
