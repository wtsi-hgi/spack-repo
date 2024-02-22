# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestry(RPackage):
	"""Reshape Data Tree

	A series of utility functions to help with 
    reshaping hierarchy of data tree, and reform the structure of data tree. 
	"""
	
	cran = "forestry" 

	version("0.1.1", md5="dd97cb669a9c7d376b03baec9d705794")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
