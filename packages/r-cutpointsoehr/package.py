# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCutpointsoehr(RPackage):
	"""Optimal Equal-HR Method to Find Two Cutpoints for U-Shaped
Relationships in Cox Model

	Use optimal equal-HR method to determine two optimal cutpoints of a continuous predictor that has a U-shaped relationship with survival outcomes based on Cox regression model. The optimal equal-HR method estimates two optimal cut-points that have approximately the same log hazard value based on Cox regression model and divides individuals into different groups according to their HR values.
	"""
	
	cran = "CutpointsOEHR" 

	version("0.1.2", md5="4b7dcdda74695e8be84983365ccb308d")

	depends_on("r-survival", type=("build", "run"))
