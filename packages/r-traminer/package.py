# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraminer(RPackage):
	"""Trajectory Miner: a Sequence Analysis Toolkit

	Set of sequence analysis tools for manipulating, describing and rendering categorical sequences, and more generally mining sequence data in the field of social sciences. Although this sequence analysis package is primarily intended for state or event sequences that describe time use or life courses such as family formation histories or professional careers, its features also apply to many other kinds of categorical sequence data. It accepts many different sequence representations as input and provides tools for converting sequences from one format to another. It offers several functions for describing and rendering sequences, for computing distances between sequences with different metrics (among which optimal matching), original dissimilarity-based analysis tools, and functions for extracting the most frequent event subsequences and identifying the most discriminating ones among them. A user's guide can be found on the TraMineR web page.
	"""
	
	homepage = "http://traminer.unige.ch"
	cran = "TraMineR" 

	version("2.2-9", md5="23f6dcf0e61147e01a2bf55cec33d713")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
