# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHybridogram(RPackage):
	"""Function that Creates a Heat Map from Hybridization Data

	Using hybrid data, this package created a vividly colored hybrid heat map.
    The input is two files which are auto-selected.
    The first file has three columns, the first two for pairs of species,
    with the third column for the hybrid experiment code (an integer).
    The second file is a list of code and their descriptions in two 
    columns. The output is a figure showing the hybrid heat map with a color legend.
	"""
	
	cran = "hybridogram" 

	version("0.3.2", md5="3d749115a37b3f5bf23ed384ff3e26ea")

	depends_on("r-pheatmap", type=("build", "run"))
