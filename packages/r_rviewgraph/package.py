# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRviewgraph(RPackage):
	"""Animated Graph Layout Viewer

	Provides 'Java' graphical user interfaces 
    for viewing, manipulating and plotting graphs. 
    Graphs may be directed or undirected.
	"""
	
	cran = "rviewgraph" 

	version("1.4.2", md5="22d82094dead4e09f8afebb409858960")

	depends_on("r-rjava", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
