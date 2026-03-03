# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeniusr(RPackage):
	"""Tools for Working with the 'Genius' API

	Provides tools to interact nicely with the 'Genius' API 
    <https://docs.genius.com/>. 
    Search hosted content, extract associated metadata and retrieve lyrics with ease.
	"""
	
	homepage = "https://ewenme.github.io/geniusr/"
	cran = "geniusr" 

	version("1.2.1", md5="f19b35c3d0c0647e63ce8301483b7979")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
