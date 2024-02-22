# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmdatabase(RPackage):
	"""Accessing a Geometallurgical Database with R

	A template for a geometallurgical database and a fast and easy
    interface for accessing it is provided in this package.
	"""
	
	homepage = "http://www.r-project.org"
	cran = "gmDatabase" 

	version("0.5.0", md5="007733a04529c4a4ec85483b09d55905")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rmysql", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
