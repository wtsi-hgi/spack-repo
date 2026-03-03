# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRquake(RPackage):
	"""Seismic Hypocenter Determination

	Non-linear inversion for hypocenter estimation and analysis of seismic data collected continuously, or in trigger mode. The functions organize other functions from 'RSEIS' and 'GEOmap' to help researchers pick, locate, and store hypocenters for detailed seismic investigation. Error ellipsoids and station influence are estimated via jackknife analysis. References include  Iversen, E. S., and J. M. Lees (1996)<doi:10.1785/BSSA0860061853>.
	"""
	
	cran = "Rquake" 

	version("2.5-1", md5="b89d3663f6c91123b6b1874082c97c06")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rpmg", type=("build", "run"))
	depends_on("r-rseis", type=("build", "run"))
	depends_on("r-geomap", type=("build", "run"))
	depends_on("r-mba", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
