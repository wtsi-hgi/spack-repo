# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsindependencetest(RPackage):
	"""Independence Tests for Two-Way, Three-Way and Four-Way
Contingency Tables

	Presentation two independence tests for two-way, three-way and four-way contingency tables. These tests are: the modular test and the logarithmic minimum test. For details on this method see: Sulewski (2017) <doi:10.18778/0208-6018.330.04>, Sulewski (2018) <doi:10.1080/02664763.2018.1424122>, Sulewski (2019) <doi:10.2478/bile-2019-0003>, Sulewski (2021) <doi:10.1080/00949655.2021.1908286>.
	"""
	
	cran = "PSIndependenceTest" 

	version("0.0.1", md5="3f672be4e0a665b093b163c1c78c7b4d")

	depends_on("r@3.5:", type=("build", "run"))
