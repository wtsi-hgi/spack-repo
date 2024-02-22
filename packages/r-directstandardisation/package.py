# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirectstandardisation(RPackage):
	"""Adjusted Means and Proportions by Direct Standardisation

	Calculate adjusted means and proportions of a variable by groups defined by another variable by direct standardisation, standardised to the structure of the dataset.
	"""
	
	cran = "DirectStandardisation" 

	version("1.3", md5="edaf3773226505ce739aa3f373d3118c")

