# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROutcomerate(RPackage):
	"""AAPOR Survey Outcome Rates

	Standardized survey outcome rate functions, including the response rate, contact rate, cooperation rate, and refusal rate. These outcome rates allow survey researchers to measure the quality of survey data using definitions published by the American Association of Public Opinion Research (AAPOR). For details on these standards, see AAPOR (2016) <https://www.aapor.org/Standards-Ethics/Standard-Definitions-(1).aspx>. 
	"""
	
	homepage = "https://github.com/ropensci/outcomerate"
	cran = "outcomerate" 

	version("1.0.1", md5="dd5271dc1c7d828bc6b793f01a77c325")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
