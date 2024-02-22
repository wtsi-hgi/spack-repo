# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoss(RPackage):
	"""Multi-Omic Integration via Sparse Singular Value Decomposition

	High dimensionality, noise and heterogeneity among
    samples and features challenge the omic integration task. Here we
    present an omic integration method based on sparse singular value
    decomposition (SVD) to deal with these limitations, by: a. obtaining
    the main axes of variation of the combined omics, b. imposing sparsity
    constraints at both subjects (rows) and features (columns) levels
    using Elastic Net type of shrinkage, and c. allowing both linear and
    non-linear projections (via t-Stochastic Neighbor Embedding) of the
    omic data to detect clusters in very convoluted data
    (Gonzalez-Reymundez et. al, 2022) <doi:10.1093/bioinformatics/btac179>.
	"""
	
	homepage = "https://github.com/agugonrey/MOSS"
	cran = "MOSS" 

	version("0.2.2", md5="1f70372d78e9026a1a4357b10ce65b53")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
