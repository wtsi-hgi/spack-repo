# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoonbook(RPackage):
	"""Functions and Datasets for the Book by Keon-Woong Moon

	Several analysis-related functions for the book entitled "R
    statistics and graph for medical articles" (written in Korean), version 1,
    by Keon-Woong Moon with Korean demographic data with several plot
    functions.
	"""
	
	homepage = "https://github.com/cardiomoon/moonBook"
	cran = "moonBook" 

	version("0.3.1", md5="8bce7b205a9a676bfddbd568ec8337b9")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-sjmisc", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
