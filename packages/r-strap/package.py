# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrap(RPackage):
	"""Stratigraphic Tree Analysis for Palaeontology

	Functions for the stratigraphic analysis of phylogenetic trees.
	"""
	
	cran = "strap" 

	version("1.6-0", md5="f1d88fdaaff0570774ddc741b35a0f4e")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-geoscale", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
