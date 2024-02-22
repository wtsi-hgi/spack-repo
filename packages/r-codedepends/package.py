# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodedepends(RPackage):
	"""Analysis of R Code for Reproducible Research and Code
Comprehension

	Tools for analyzing R expressions
  or blocks of code and determining the dependencies between them.
  It focuses on R scripts, but can be used on the bodies of functions.
  There are many facilities including the ability to summarize  or get a high-level
  view of code, determining dependencies between variables,  code improvement
  suggestions.
	"""
	
	homepage = "https://github.com/duncantl/CodeDepends"
	cran = "CodeDepends" 

	version("0.6.5", md5="38607e02a9e73050489f06dec43c9929")

	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
