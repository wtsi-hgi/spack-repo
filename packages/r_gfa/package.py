# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfa(RPackage):
	"""Group Factor Analysis

	Factor analysis implementation for multiple data sources, i.e., for groups of variables. The whole data analysis pipeline is provided, including functions and recommendations for data normalization and model definition, as well as missing value prediction and model visualization. The model group factor analysis (GFA) is inferred with Gibbs sampling, and it has been presented originally by Virtanen et al. (2012), and extended in Klami et al. (2015) <DOI:10.1109/TNNLS.2014.2376974> and Bunte et al. (2016) <DOI:10.1093/bioinformatics/btw207>; for details, see the citation info.
	"""
	
	cran = "GFA" 

	version("1.0.5", md5="120596244929ae4a15d1266567bc2b75")

