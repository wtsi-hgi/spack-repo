# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpolyhedra(RPackage):
	"""Polyhedra Database

	A polyhedra database scraped from various sources as R6 objects and 'rgl' visualizing capabilities.
	"""
	
	homepage = "https://docs.ropensci.org/Rpolyhedra/"
	cran = "Rpolyhedra" 

	version("0.5.4", md5="9f5bf5a3ff05338bee46d9d858bf415d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
