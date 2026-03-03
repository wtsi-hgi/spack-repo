# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTranslated(RPackage):
	"""Simple and Robust Translation System

	Allows translating with formatted string literals, grouped entries, and configurable system of plurals. Have a separate file for each locale and use inheritance to handle dialect differences.
	"""
	
	homepage = "https://github.com/ttscience/translated"
	cran = "translated" 

	version("0.1.1", md5="8a41c281183891800952ca04c14d3ff3")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
