# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwimmer(RPackage):
	"""Data Import, Cleaning, and Conversions for Swimming Results

	The goal of the 'SwimmeR' package is to provide means of acquiring, and then analyzing, data from swimming (and diving) competitions.  To that end 'SwimmeR' allows results to be read in from .html sources, like 'Hy-Tek' real time results pages, '.pdf' files, 'ISL' results, 'Omega' results, and (on a development basis) '.hy3' files.  Once read in, 'SwimmeR' can convert swimming times (performances) between the computationally useful format of seconds reported to the '100ths' place (e.g. 95.37), and the conventional reporting format (1:35.37) used in the swimming community.  'SwimmeR' can also score meets in a variety of formats with user defined point values, convert times between courses ('LCM', 'SCM', 'SCY') and draw single elimination brackets, as well as providing a suite of tools for working cleaning swimming data.  This is a developmental package, not yet mature.
	"""
	
	cran = "SwimmeR" 

	version("0.14.2", md5="a901b3d750fa39a5790f46cd9f19c831")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
