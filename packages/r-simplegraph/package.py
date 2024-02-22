# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplegraph(RPackage):
	"""Simple Graph Data Types and Basic Algorithms

	Simple classic graph algorithms for simple graph classes.
    Graphs may possess vertex and edge attributes. 'simplegraph' has
    no dependencies and it is written entirely in R, so it is easy to
    install.
	"""
	
	homepage = "https://github.com/gaborcsardi/simplegraph"
	cran = "simplegraph" 

	version("1.0.1", md5="faa749f15b45e093f7ebb93ebe1767fb")

