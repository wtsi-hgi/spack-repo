# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondensr(RPackage):
	"""Academic Group Website Generator

	Helps automate 'Quarto' website creation for small academic groups.
    Builds a database-like structure of people, projects and publications, linking
    them together with a string-based ID system. Then, provides functions to automate
    production of clean markdown for these structures, and in-built CSS formatting
    using CSS flexbox.
	"""
	
	homepage = "http://www.michaellydeamore.com/condensr/"
	cran = "condensr" 

	version("1.0.0", md5="5a320ea112cf0d6e6f2438f494ed0764")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
