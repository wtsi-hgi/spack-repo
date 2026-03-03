# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDggridr(RPackage):
	"""Discrete Global Grids

	Spatial analyses involving binning require that every bin have the same area, but this is impossible using a rectangular grid laid over the Earth or over any projection of the Earth. Discrete global grids use hexagons, triangles, and diamonds to overcome this issue, overlaying the Earth with equally-sized bins. This package provides utilities for working with discrete global grids, along with utilities to aid in plotting such data.
	"""
	
	homepage = "https://github.com/r-barnes/dggridR/"
	cran = "dggridR" 

	version("3.0.0", md5="ea9dc2501643f121fdd5d811ec525f9b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.4:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-sp@1.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
