# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialeco(RPackage):
	"""Spatial Analysis and Modelling Utilities.

	Utilities to support spatial data manipulation, query, sampling and
	modelling. Functions include models for species population density,
	download utilities for climate and global deforestation spatial products,
	spatial smoothing, multivariate separability, point process model for
	creating pseudo- absences and sub-sampling, polygon and point-distance
	landscape metrics, auto-logistic model, sampling models, cluster
	optimization, statistical exploratory tools and raster-based metrics."""

	cran = "spatialEco"
	version("2.0-2", md5="29a40c2bd6ac5ae8562b653bbe8ffcf8")
	version("2.0-0", sha256="9a2384e875ec465d1a2ccd392acc90d4469eb62babd32bb90e30b27a921153f6")
	version("1.3-7", sha256="38688466d9a2a56675e2fe45cf69833a163133ad3afb6f95e9ac2e8eab221b7a")
	version("1.3-5", sha256="d4fb211124edf828333841c44a5af01165c53d89af460144214d81e3c13983c7")
	version("1.3-2", sha256="9dfa427ee8b112446b582f6739a1c40a6e3ad3d050f522082a28ce47c675e57a")
	version("1.3-1", sha256="ff12e26cc1bbf7934fbf712c99765d96ce6817e8055faa15a26d9ebade4bbf1c")
	version("1.3-0", sha256="cfa09673cb3bbed30b243082fc2d63ac09f48b9f072a18d32b95c2c29979d1d0")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
