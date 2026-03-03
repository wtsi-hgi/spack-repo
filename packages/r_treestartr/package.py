# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreestartr(RPackage):
	"""Generate Starting Trees for Combined Molecular, Morphological
and Stratigraphic Data

	Combine a list of taxa with a phylogeny to generate a starting tree for use in
    total evidence dating analyses.
	"""
	
	homepage = "https://ropensci.github.io/treeStartR/"
	cran = "treestartr" 

	version("0.1.0", md5="d0071c01ab1d7833641fb957e711e306")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-phytools@0.6.4:", type=("build", "run"))
	depends_on("r-ape@5:", type=("build", "run"))
