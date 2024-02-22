# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRivernet(RPackage):
	"""Read, Analyze and Plot River Networks

	Functions for reading, analysing and plotting river networks.
  For this package, river networks consist of sections and nodes with associated attributes, 
  e.g. to characterise their morphological, chemical and biological state.
  The package provides functions to read this data from text files, to analyse the network
  structure and network paths and regions consisting of sections and nodes that fulfill
  prescribed criteria, and to plot the river network and associated properties.
	"""
	
	cran = "rivernet" 

	version("1.2.3", md5="4cdc5e7d1f0850930c13c7b079ba6162")

