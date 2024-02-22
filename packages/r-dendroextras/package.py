# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDendroextras(RPackage):
	"""Extra Functions to Cut, Label and Colour Dendrogram Clusters

	Provides extra functions to manipulate dendrograms
    that build on the base functions provided by the 'stats' package. The main
    functionality it is designed to add is the ability to colour all the edges
    in an object of class 'dendrogram' according to cluster membership i.e. each
    subtree is coloured, not just the terminal leaves. In addition it provides
    some utility functions to cut 'dendrogram' and 'hclust' objects and to 
    set/get labels.
	"""
	
	cran = "dendroextras" 

	version("0.2.3", md5="1ed7012ca6e1975edc925fd34ae8781f")

