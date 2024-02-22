# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComfuncs(RPackage):
	"""Commonly Used Functions for R Shiny Applications

	A set of common functions to be used for displaying messages, checking variables, 
  finding absolute paths, starting applications, etc. More functions will be added later.
	"""
	
	homepage = "https://github.com/TuCai/comFuncs"
	cran = "comFuncs" 

	version("0.0.6", md5="0fb5df32ea682b6b533eca832d6076eb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny@1.3.2:", type=("build", "run"))
