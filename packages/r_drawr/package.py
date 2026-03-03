# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrawr(RPackage):
	"""Discriminative Random Walk with Restart

	We present DRaWR, a network-based method for ranking genes or
    properties related to a given gene set. Such related genes or properties are
    identified from among the nodes of a large, heterogeneous network of biological
    information. Our method involves a random walk with restarts, performed on
    an initial network with multiple node and edge types, preserving more of the
    original, specific property information than current methods that operate
    on homogeneous networks. In this first stage of our algorithm, we find the
    properties that are the most relevant to the given gene set and extract a
    subnetwork of the original network, comprising only the relevant properties. We
    then rerank genes by their similarity to the given gene set, based on a second
    random walk with restarts, performed on the above subnetwork.
	"""
	
	cran = "DRaWR" 

	version("1.0.3", md5="a54cac0743907c2c4d852048492ef154")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
