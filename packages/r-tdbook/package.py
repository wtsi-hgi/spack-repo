# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdbook(RPackage):
	"""Companion Package for the Book "Data Integration, Manipulation
and Visualization of Phylogenetic Trees" by Guangchuang Yu
(2022, ISBN:9781032233574)

	The companion package that provides all the datasets used in the book
 "Data Integration, Manipulation and Visualization of Phylogenetic Trees" by Guangchuang Yu (2022, ISBN:9781032233574).
	"""
	
	homepage = "https://www.amazon.com/Integration-Manipulation-Visualization-Phylogenetic-Computational-ebook/dp/B0B5NLZR1Z/"
	cran = "TDbook" 

	version("0.0.6", md5="3cbecccfead6a413c8d51883f05b4ede")

	depends_on("r@3.5:", type=("build", "run"))
