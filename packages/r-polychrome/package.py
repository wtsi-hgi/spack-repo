# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolychrome(RPackage):
	"""Qualitative Palettes with Many Colors

	Tools for creating, viewing, and assessing qualitative
 palettes with many (20-30 or more) colors. See Coombes and colleagues
 (2019) <doi:10.18637/jss.v090.c01>.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "Polychrome" 

	version("1.5.1", md5="884d7e7cabb5419dcda496678f310083")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
