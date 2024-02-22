# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomap(RPackage):
	"""Topographic and Geologic Mapping

	Set of routines for making map projections (forward and inverse), topographic maps, perspective plots, geological maps, geological map symbols, geological databases, interactive plotting and selection of focus regions.
	"""
	
	cran = "GEOmap" 

	version("2.5-5", md5="f24aae5a7eb4f18d67db573e5472db09")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rpmg", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-mba", type=("build", "run"))
