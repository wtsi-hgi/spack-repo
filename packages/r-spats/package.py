# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpats(RPackage):
	"""Spatial Analysis of Field Trials with Splines

	Analysis of field trial experiments by modelling spatial trends using two-dimensional Penalised spline (P-spline) models.
	"""
	
	cran = "SpATS" 

	version("1.0-18", md5="3671f91c25b8085d9e4bf0c6d43476e8")

	depends_on("r-fields", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
