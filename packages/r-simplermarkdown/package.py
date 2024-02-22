# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplermarkdown(RPackage):
	"""Simple Engine for Generating Reports using R

	Runs R-code present in a pandoc markdown file and 
  includes the resulting output in the resulting markdown file. This
  file can then be converted into any of the output formats 
  supported by pandoc. The package can also be used as an engine
  for writing package vignettes. 
	"""
	
	homepage = "https://github.com/djvanderlaan/simplermarkdown"
	cran = "simplermarkdown" 

	version("0.0.6", md5="a692f54b8cdb625a3472b8f82fe2bd42")

	depends_on("r-rjson", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
