# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBossa(RPackage):
	"""A Bunch of Structure and Sequence Analysis

	Reads and plots phylogenetic placements.
	"""
	
	cran = "BoSSA" 

	version("3.7", md5="36bcf89809870aa8a97621d93c344ae7")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
