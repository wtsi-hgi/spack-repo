# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
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

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
