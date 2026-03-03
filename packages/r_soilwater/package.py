# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoilwater(RPackage):
	"""Implementation of Parametric Formulas for Soil Water Retention
or Conductivity Curve

	It implements parametric formulas of soil
    water retention or conductivity curve. At the moment, only Van Genuchten
    (for soil water retention curve) and Mualem (for hydraulic conductivity)
    were implemented. 
    See reference (<http://en.wikipedia.org/wiki/Water_retention_curve>).
	"""
	
	homepage = "https://github.com/ecor/soilwater"
	cran = "soilwater" 

	version("1.0.5", md5="17a6157ee360d717db7659d2bdae0d66")

