# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultirdpg(RPackage):
	"""Multiple Random Dot Product Graphs

	Fits the Multiple Random Dot Product Graph Model and performs a test
	 for whether two networks come from the same distribution. Both methods are 
	 proposed in Nielsen, A.M., Witten, D., (2018) "The Multiple Random Dot Product Graph
	 Model", arXiv preprint <arXiv:1811.12172> (Submitted to Journal of Computational
	 and Graphical Statistics).
	"""
	
	cran = "multiRDPG" 

	version("1.0.1", md5="d0d5920b7c1d40d063118b5e27cd8f9e")

