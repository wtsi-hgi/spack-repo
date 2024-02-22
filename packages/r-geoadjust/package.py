# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeoadjust(RPackage):
	"""Accounting for Random Displacements of True GPS Coordinates of
Data

	The purpose is to account for the random displacements 
 (jittering) of true survey household cluster center coordinates in geostatistical 
 analyses of Demographic and Health Surveys program (DHS) data. Adjustment for 
 jittering can be implemented either in the spatial random effect, or in the 
 raster/distance based covariates, or in both. Detailed information about the methods 
 behind the package functionality can be found in two preprints.
 Umut Altay, John Paige, Andrea Riebler, Geir-Arne Fuglstad (2022) <arXiv:2202.11035v2>. 
 Umut Altay, John Paige, Andrea Riebler, Geir-Arne Fuglstad (2022) <arXiv:2211.07442v1>. 
	"""
	
	cran = "GeoAdjust" 

	version("2.0.0", md5="0c73c86cc77a5ebd8033a74ddc769bc1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fmesher", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-summer", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
