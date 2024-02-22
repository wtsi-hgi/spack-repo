# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObjectremover(RPackage):
	"""'RStudio' Addin for Removing Objects from the Global Environment
Based on Patterns and Object Type

	An 'RStudio' addin to assist with removing objects from the global environment. Features include removing objects according to name patterns and object type. During the course of an analysis, temporary objects are often created and this tool assists with removing them quickly. This can be useful when memory management within 'R' is important.
	"""
	
	homepage = "https://github.com/alan-y/objectremover"
	cran = "objectremover" 

	version("0.8.1", md5="200b4a3931edbb0358eadeda47bd1a17")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
