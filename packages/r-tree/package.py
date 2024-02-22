# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTree(RPackage):
	"""Classification and Regression Trees

	Classification and regression trees.
	"""
	
	cran = "tree" 

	version("1.0-43", md5="7afb91c0210ef420567d7188f5719633")

	depends_on("r@3.6:", type=("build", "run"))
