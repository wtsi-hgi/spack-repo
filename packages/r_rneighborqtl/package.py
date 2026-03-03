# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRneighborqtl(RPackage):
	"""Interval Mapping for Quantitative Trait Loci Underlying Neighbor
Effects

	To enable quantitative trait loci mapping of neighbor effects, this package extends a single-marker regression to interval mapping. The theoretical background of the method is described in Sato et al. (2021) <doi:10.1093/g3journal/jkab017>.
	"""
	
	cran = "rNeighborQTL" 

	version("1.1.2", md5="1bbd085b38d08e8102d68b538fdc4f3e")

	depends_on("r-gaston", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
