# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirectotree(RPackage):
	"""Creates an Interactive Tree Structure of a Directory

	Represents the content of a directory as an interactive collapsible tree. Offers
    the possibility to assign a text (e.g., a 'Readme.txt') to each folder
    (represented as a clickable node), so that when the user hovers the pointer
    over a node, the corresponding text is displayed as a tooltip.
	"""
	
	cran = "directotree" 

	version("1.0.0", md5="40f0ee0dcaa25b1a8b4c921e913fb732")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-collapsibletree@0.1.6:", type=("build", "run"))
	depends_on("r-data-tree@0.7.6:", type=("build", "run"))
