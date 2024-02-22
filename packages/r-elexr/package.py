# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElexr(RPackage):
	"""Load Associated Press Election Results with Elex

	Provides R access to election results data. Wraps elex (https://github.com/newsdev/elex/), a Python package and command line tool for fetching and parsing Associated Press election results.
	"""
	
	cran = "elexr" 

	version("1.0", md5="354153bd8052d09bfdd9d47ffd46bafc")

	depends_on("python@3.5:", type=("build", "link", "run"))
