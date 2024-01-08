# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RUmap(RPackage):
	"""Uniform Manifold Approximation and Projection

	Uniform manifold approximation and projection is a technique
    for dimension reduction. The algorithm was described by McInnes and
    Healy (2018) in <arXiv:1802.03426>. This package provides an interface
    for two implementations. One is written from scratch, including components
    for nearest-neighbor search and for embedding. The second implementation
    is a wrapper for 'python' package 'umap-learn' (requires separate
    installation, see vignette for more details).
	"""
	
	homepage = "https://github.com/tkonopka/umap"
	cran = "umap" 

	version("0.2.10.0", md5="d996b2627ec6bba2136ee0d099b4ab6c")

	depends_on("r@3.6.0:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rcpp@0.12.6:", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
