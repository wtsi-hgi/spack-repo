# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSara4r(RPackage):
	"""An R-GUI for Spatial Analysis of Surface Runoff using the
NRCS-CN Method

	A Graphical user interface to calculate the rainfall-runoff relation using the Natural Resources Conservation Service - Curve Number method (NRCS-CN method) but include modifications by Hawkins et al., (2002) about the Initial Abstraction. This GUI follows the programming logic of a previously published software (Hernandez-Guzman et al., 2011)<doi:10.1016/j.envsoft.2011.07.006>. It is a raster-based GIS tool that outputs runoff estimates from Land use/land cover and hydrologic soil group maps.
    This package has already been published in Journal of Hydroinformatics (Hernandez-Guzman et al., 2021)<doi:10.2166/hydro.2020.087> but it is under constant development at the Institute about Natural Resources Research (INIRENA) from the Universidad Michoacana de San Nicolas de Hidalgo and represents a collaborative effort between the Hydro-Geomatic Lab (INIRENA) with the Environmental Management Lab (CIAD, A.C.).
	"""
	
	homepage = "https://hydro-geomatic-lab.com/"
	cran = "sara4r" 

	version("0.1.0", md5="ba25831fc74957bcfab704feafc2f604")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
