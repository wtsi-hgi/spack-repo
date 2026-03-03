# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValentine(RPackage):
	"""Spread the Love for R Packages with Poetry

	Uses 'ChatGPT' <https://openai.com/> to create poems about R packages.
   Currently contains the roses() function to make "roses are red, ..." style 
   poems and the prompt() function to only assemble the prompt without submitting 
   it to 'ChatGPT'. 
	"""
	
	homepage = "https://github.com/tadascience/valentine"
	cran = "valentine" 

	version("2024.2.14", md5="0856b2e63b45563e826c82c9d7e2f8c7")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-openai", type=("build", "run"))
