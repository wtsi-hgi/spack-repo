# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmdhelpers(RPackage):
	"""Helper Functions for Rmd Documents

	A series of functions to aid in repeated tasks for Rmd documents. All details are to my personal preference, though I am happy to add flexibility if there are use cases I am missing. I will continue updating with new functions as I add utility functions for myself.
	"""
	
	cran = "rmdHelpers" 

	version("1.2", md5="1fa88360e9f14aa11a012c23735f3048")

	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
