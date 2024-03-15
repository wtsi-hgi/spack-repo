# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGstat(RPackage):
	"""Spatial and Spatio-Temporal Geostatistical Modelling, Predictionand
	Simulation.

	Variogram modelling; simple, ordinary and universal point or block
	(co)kriging; spatio-temporal kriging; sequential Gaussian or indicator
	(co)simulation; variogram and variogram map plotting utility functions;
	supports sf and stars."""

	cran = "gstat"

	license("GPL-2.0-or-later")

	version("2.1-1", md5="549094cfc1d3acd39a6f532a0fdfad9a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-sp@0.9.72:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-sf@0.7.2:", type=("build", "run"))
	depends_on("r-sftime", type=("build", "run"))
	depends_on("r-spacetime@1.2.8:", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
