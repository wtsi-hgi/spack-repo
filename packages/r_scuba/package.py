# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScuba(RPackage):
	"""Diving Calculations and Decompression Models

	Code for describing and manipulating scuba diving profiles 
	(depth-time curves) and decompression models, 
        for calculating the predictions of decompression models,
	for calculating maximum no-decompression time and decompression tables,
	and for performing mixed gas calculations. 
	"""
	
	cran = "scuba" 

	version("1.11-1", md5="853c5fa8654d1467c1eb91a2b3c87b44")

	depends_on("r@3.5:", type=("build", "run"))
