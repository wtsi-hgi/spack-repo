# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeopleanalytics(RPackage):
	"""Data Sets for Craig Starbuck's Book, "The Fundamentals of People
Analytics: With Applications in R"

	Data sets associated with modeling examples in Craig Starbuck's book, "The Fundamentals of People Analytics: With Applications in R".
	"""
	
	cran = "peopleanalytics" 

	version("0.1.0", md5="e750df777b162f2d084b2b90bed41b92")

	depends_on("r@3.5:", type=("build", "run"))
