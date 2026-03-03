# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapsrinteractive(RPackage):
	"""Local Adaptation and Evaluation of Raster Maps

	Local adaptation and evaluation of maps of continuous attributes in raster format by use of point location data.
	"""
	
	homepage = "https://CRAN.R-project.org/package=mapsRinteractive"
	cran = "mapsRinteractive" 

	version("2.0.1", md5="d43a852cad9015e31301baabf18fef8f")

	depends_on("r-terra", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
