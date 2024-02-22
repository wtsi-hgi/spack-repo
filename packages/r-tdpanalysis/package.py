# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdpanalysis(RPackage):
	"""Granier's Sap Flow Sensors (TDP) Analysis

	Set of functions designed to help in the
    analysis of TDP sensors. Features includes dates and time conversion, weather
    data interpolation, daily maximum of tension analysis and calculations required
    to convert sap flow density data to sap flow rates at the tree and plot scale (For more information see : Granier (1985) <DOI:10.1051/forest:19850204> & Granier (1987) <DOI:10.1093/treephys/3.4.309>).
	"""
	
	cran = "TDPanalysis" 

	version("1.0", md5="8f3a950e7ca405beae30d1e7f515d97e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
