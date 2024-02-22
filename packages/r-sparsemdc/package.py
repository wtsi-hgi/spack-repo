# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsemdc(RPackage):
	"""Implementation of SparseMDC Algorithm

	Implements the algorithm described in
    Barron, M., and Li, J. (Not yet published). This algorithm clusters
    samples from multiple ordered populations, links the clusters across the
    conditions and identifies marker genes for these changes. The package was
    designed for scRNA-Seq data but is also applicable to many other data
    types, just replace cells with samples and genes with variables. The
    package also contains functions for estimating the parameters for SparseMDC
    as outlined in the paper. We recommend that users further select their
    marker genes using the magnitude of the cluster centers.
	"""
	
	cran = "SparseMDC" 

	version("0.99.5", md5="7e80dae16f96c3e4989c39650df42e0d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
