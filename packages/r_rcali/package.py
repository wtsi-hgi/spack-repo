# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcali(RPackage):
	"""Calculation of the Integrated Flow of Particles Between Polygons

	Calculate the flow of particles between polygons by two integration methods:
  integration by a cubature method and integration on a grid of points.
  Annie Bouvier, Kien Kieu, Kasia Adamczyk and Herve Monod (2009)
  <doi:10.1016/j.envsoft.2008.11.006>.
	"""
	
	homepage = "https://gitlab.paca.inrae.fr/biosp/RCALI"
	cran = "RCALI" 

	version("0.3.6", md5="33206398d0d8f6d9ecd875285c29c534")

	depends_on("r-splancs", type=("build", "run"))
