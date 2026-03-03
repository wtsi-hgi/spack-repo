# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyradiomatrix(RPackage):
	"""Create a Matrix with Radio Buttons

	An input controller for R Shiny: a matrix with radio buttons, 
    where only one option per row can be selected.
	"""
	
	cran = "shinyRadioMatrix" 

	version("0.2.1", md5="dd2c8c2287e8119cf7c564a60791fb8b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
