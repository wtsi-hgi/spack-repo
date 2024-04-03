# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamilies(RPackage):
	"""Kinship Ties in (Virtual) Multi-Generation Populations

	Tools to study lineages, grandparenthood, loss of close relatives, kinship networks and other topics in multi-generation populations.
	"""
	
	cran = "Families" 

	version("1.0.1", md5="8e006a7d5f60c512aae9d3f08cf86188")
	version("2.0.1", md5="40e0911daad716119d5043db89226ab8")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
