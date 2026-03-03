# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApcluster(RPackage):
	"""Affinity Propagation Clustering

	Implements Affinity Propagation clustering introduced by Frey and
	Dueck (2007) <DOI:10.1126/science.1136800>. The algorithms are largely
        analogous to the 'Matlab' code published by Frey and Dueck.
        The package further provides leveraged affinity propagation and an
        algorithm for exemplar-based agglomerative clustering that can also be
        used to join clusters obtained from affinity propagation. Various
        plotting functions are available for analyzing clustering results.
	"""
	
	homepage = "http://www.bioinf.jku.at/software/apcluster/"
	cran = "apcluster" 

	version("1.4.11", md5="53208e07a78a91acd131d4aa8d22f6e0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
