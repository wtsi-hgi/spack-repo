# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAustralianpoliticians(RPackage):
	"""Provides Datasets About Australian Politicians

	Provides access to biographical and political data about Australian 
    federal politicians who served between 1901 and 2021. This enhances how 
    reproducible research is that uses this data.
	"""
	
	homepage = "https://github.com/RohanAlexander/AustralianPoliticians"
	cran = "AustralianPoliticians" 

	version("0.1.0", md5="43ee70fd84abed50a48044ef5bec2d80")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
