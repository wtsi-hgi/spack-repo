# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeps(RPackage):
	"""Dependency Management with 'roxygen'-Style Comments

	Manage your source code dependencies
  by decorating your existing R code with special,
  'roxygen'-style comments.
	"""
	
	homepage = "https://github.com/analythium/deps"
	cran = "deps" 

	version("0.2.0", md5="bdaf6a06ae9871b0b489783ad22a46ff")

	depends_on("r-renv", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
