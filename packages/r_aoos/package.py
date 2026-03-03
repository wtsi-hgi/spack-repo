# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAoos(RPackage):
	"""Another Object Orientation System

	Another implementation of object-orientation in R. It provides
    syntactic sugar for the S4 class system and two alternative new
    implementations. One is an experimental version built around S4
    and the other one makes it more convenient to work with lists as objects.
	"""
	
	homepage = "https://wahani.github.io/aoos"
	cran = "aoos" 

	version("0.5.0", md5="365220d20ccd7075fa4942459f3f2780")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
