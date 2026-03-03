# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdd(RPackage):
	"""Easy Manipulation of Out of Memory Data Sets

	Hard drive data: Class of data allowing the easy importation/manipulation of out of memory data sets. The data sets are located on disk but look like in-memory, the syntax for manipulation is similar to 'data.table'. Operations are performed "chunk-wise" behind the scene.
	"""
	
	cran = "hdd" 

	version("0.1.1", md5="dbf91e901dcb3783e72d94719858689b")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dreamerr", type=("build", "run"))
