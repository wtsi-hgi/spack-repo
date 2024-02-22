# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotifcluster(RPackage):
	"""Motif-Based Spectral Clustering of Weighted Directed Networks

	
    Tools for spectral clustering of weighted directed networks using motif
    adjacency matrices. Methods perform well on large and sparse networks, and
    random sampling methods for generating weighted directed networks are also
    provided. Based on methodology detailed in Underwood, Elliott and Cucuringu
    (2020) <arXiv:2004.01293>.
	"""
	
	homepage = "https://github.com/wgunderwood/motifcluster"
	cran = "motifcluster" 

	version("0.2.3", md5="e89339b6837ca8fe6663b8350a9bd133")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph@1.2.5:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
	depends_on("r-rspectra@0.16:", type=("build", "run"))
