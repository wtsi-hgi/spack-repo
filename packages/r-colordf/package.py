# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColordf(RPackage):
	"""Colorful Data Frames in R Terminal

	Colorful Data Frames in the terminal. The new class does
             change the behaviour of any of the objects, but adds a style
             definition and a print method. Using ANSI escape codes, it
             colors the terminal output of data frames. Some column types
             (such as p-values and identifiers) are automatically
             recognized.
	"""
	
	homepage = "https://january3.github.io/colorDF/"
	cran = "colorDF" 

	version("0.1.7", md5="0dbab927167af22d986c1ad04e2044b2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
