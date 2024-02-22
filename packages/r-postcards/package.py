# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPostcards(RPackage):
	"""Create Beautiful, Simple Personal Websites

	A collection of R Markdown templates for creating simple and easy 
  to personalize single page websites.
	"""
	
	homepage = "https://github.com/seankross/postcards"
	cran = "postcards" 

	version("0.2.3", md5="0690b76f60216d1b4c7cf553227ce59c")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
