# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoodlequizr(RPackage):
	"""Easily Create Fully Randomized 'Moodle' Test Questions

	Routines to generate fully randomized 'moodle' quizzes. It also contains 12 examples and a 'shiny' app.
	"""
	
	cran = "moodlequizR" 

	version("1.0.3", md5="bad6895bc26beae994975a4d7d667bf6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-base64", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
