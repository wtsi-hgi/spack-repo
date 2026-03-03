# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomod(RPackage):
	"""A Computer Program for Geotechnical Investigations

	The 'geomod' does spatial prediction of the Geotechnical soil properties. 
    It predicts the spatial distribution of Geotechnical properties of soil e.g. shear strength, 
    permeability, plasticity index, Standard Penetration Test (SPT) counts, etc. The output of the prediction takes the form of a 
    map or a series of maps. It uses the interpolation technique where a single or statistically “best” 
    estimate of spatial occurrence soil property is determined. The interpolation is based on both the 
    sampled data and a variogram model for the spatial correlation of the sampled data. 
    The single estimate is produced by a Kriging technique.
	"""
	
	cran = "geomod" 

	version("0.1.0", md5="aa05dcfbf899fa62578a3125b9a783f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rastervis", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-cubist", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-qrnn", type=("build", "run"))
	depends_on("r-quantregforest", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
