# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScaffolder(RPackage):
	"""Scaffolding Interfaces to Packages in Other Programming
Languages

	Comprehensive set of tools for scaffolding R
  interfaces to modules, classes, functions, and documentations
  written in other programming languages, such as 'Python'.
	"""
	
	homepage = "https://github.com/terrytangyuan/scaffolder"
	cran = "scaffolder" 

	version("0.0.1", md5="351057b958605f6ce6609660e48d61ae")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("python@2.7:", type=("build", "link", "run"))
