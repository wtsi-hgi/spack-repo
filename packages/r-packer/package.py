# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPacker(RPackage):
	"""An Opinionated Framework for Using 'JavaScript'

	
  Enforces good practice and provides convenience functions to make work with 'JavaScript' 
  not just easier but also scalable. It is a robust wrapper to 'NPM', 'yarn', and 'webpack' that 
  enables to compartmentalize 'JavaScript' code, leverage 'NPM' and 'yarn' packages, include
  'TypeScript', 'React', or 'Vue' in web applications, and much more.
	"""
	
	homepage = "https://github.com/JohnCoene/packer"
	cran = "packer" 

	version("0.1.3", md5="585af52c1fd77c646f21775a59ab2ab2")

	depends_on("r-fs", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
