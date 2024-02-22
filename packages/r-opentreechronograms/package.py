# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpentreechronograms(RPackage):
	"""Open Tree of Life Chronograms

	Chronogram database constructed from Open Tree of Life's phylogenetic store.
	"""
	
	cran = "OpenTreeChronograms" 

	version("2022.1.28", md5="6a9cd2c75de5a244d753bb9573b7b645")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-knitcitations", type=("build", "run"))
	depends_on("r-paleotree", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rotl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-taxize", type=("build", "run"))
	depends_on("r-treebase", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
