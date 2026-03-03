# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwirlify(RPackage):
	"""A Toolbox for Writing 'swirl' Courses

	A set of tools for writing and sharing interactive courses
    to be used with swirl.
	"""
	
	homepage = "http://swirlstats.com"
	cran = "swirlify" 

	version("0.5.3", md5="74ec6fc707da5b14823ba6cbdedcab8c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-swirl@2.4.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
