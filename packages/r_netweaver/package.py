# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetweaver(RPackage):
	"""Graphic Presentation of Complex Genomic and Network Data
Analysis

	Implements various simple function utilities and flexible pipelines to generate circular images for visualizing complex genomic and network data analysis features.
	"""
	
	homepage = "https://github.com/mw201608/NetWeaver/"
	cran = "NetWeaver" 

	version("0.0.6", md5="225b95e39f21cbb499b4049f96250b21")

	depends_on("r@3.3:", type=("build", "run"))
