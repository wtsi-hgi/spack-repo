# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptcirclust(RPackage):
	"""Circular, Periodic, or Framed Data Clustering: Fast, Optimal,
and Reproducible

	Fast, optimal, and reproducible clustering algorithms for
 circular, periodic, or framed data. The algorithms introduced here
 are based on a core algorithm for optimal framed clustering the authors
 have developed (Debnath & Song 2021) <doi:10.1109/TCBB.2021.3077573>.
 The runtime of these algorithms is O(K N log^2 N), where K is the number
 of clusters and N is the number of circular data points. On a desktop
 computer using a single processor core, millions of data points can be
 grouped into a few clusters within seconds. One can apply the algorithms
 to characterize events along circular DNA molecules, circular RNA
 molecules, and circular genomes of bacteria, chloroplast, and
 mitochondria. One can also cluster climate data along any given
 longitude or latitude. Periodic data clustering can be formulated as
 circular clustering. The algorithms offer a general high-performance
 solution to circular, periodic, or framed data clustering. 
	"""
	
	cran = "OptCirClust" 

	version("0.0.4", md5="c94299e80397b6bc7140b53b5e1a31b0")

	depends_on("r-ckmeans-1d-dp", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
