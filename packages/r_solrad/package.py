# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSolrad(RPackage):
	"""Calculating Solar Radiation and Related Variables Based on
Location, Time and Topographical Conditions

	For surface energy models and estimation of solar positions and components with varying topography, time and locations. The functions calculate solar top-of-atmosphere, open, diffuse and direct components, atmospheric transmittance and diffuse factors, day length, sunrise and sunset, solar azimuth, zenith, altitude, incidence, and hour angles, earth declination angle, equation of time, and solar constant. Details about the methods and equations are explained in Seyednasrollah, Bijan, Mukesh Kumar, and Timothy E. Link. 'On the role of vegetation density on net snow cover radiation at the forest floor.' Journal of Geophysical Research: Atmospheres 118.15 (2013): 8359-8374, <doi:10.1002/jgrd.50575>.
	"""
	
	homepage = "https://github.com/bnasr/solrad/"
	cran = "solrad" 

	version("1.0.0", md5="a59dd81df0d6782eb7ad6a5d6906e934")

	depends_on("r@3.3:", type=("build", "run"))
