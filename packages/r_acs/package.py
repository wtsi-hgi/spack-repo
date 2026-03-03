# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcs(RPackage):
	"""Download, Manipulate, and Present American Community Survey and
Decennial Data from the US Census

	Provides a general toolkit for downloading, managing,
  analyzing, and presenting data from the U.S. Census
  (<https://www.census.gov/data/developers/data-sets.html>), including
  SF1 (Decennial short-form), SF3 (Decennial long-form), and the
  American Community Survey (ACS).  Confidence intervals provided with
  ACS data are converted to standard errors to be bundled with
  estimates in complex acs objects.  Package provides new methods to
  conduct standard operations on acs objects and present/plot data in
  statistically appropriate ways.
	"""
	
	homepage = "http://dusp.mit.edu/faculty/ezra-glenn"
	cran = "acs" 

	version("2.1.4", md5="266593753bbe3c0a6023849fb768276b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
