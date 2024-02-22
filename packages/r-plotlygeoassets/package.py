# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotlygeoassets(RPackage):
	"""Render 'Plotly' Maps without an Internet Connection

	Includes 'JavaScript' files that allow 'plotly' maps to render without an internet connection.
	"""
	
	homepage = "https://github.com/cpsievert/plotlyGeoAssets"
	cran = "plotlyGeoAssets" 

	version("0.0.2", md5="6f177116fc861cef2a218ef30397b8f1")

	depends_on("r@2.10:", type=("build", "run"))
