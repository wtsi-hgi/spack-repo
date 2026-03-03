# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProtoclust(RPackage):
	"""Hierarchical Clustering with Prototypes

	Performs minimax linkage hierarchical clustering.  Every cluster
    has an associated prototype element that represents that cluster as
    described in Bien, J., and Tibshirani, R. (2011), "Hierarchical Clustering 
    with Prototypes via Minimax Linkage," The Journal of the American 
    Statistical Association, 106(495), 1075-1084.
	"""
	
	cran = "protoclust" 

	version("1.6.4", md5="06f3a4d3a917a49789c13bdc57424634")

