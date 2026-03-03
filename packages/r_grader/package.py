# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrader(RPackage):
	"""Helps Grade Assignment Submissions that are R Scripts

	After being given the location of your students' submissions and a test file, the function runs each .R file, and evaluates the results from all the given tests. Results are neatly returned in a data frame that has a row for each student, and a column for each test.
	"""
	
	cran = "gradeR" 

	version("1.0.10", md5="1e19b148b7e85c905399ec71dea7b3d2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
