# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSits(RPackage):
	"""Satellite Image Time Series Analysis for Earth Observation Data
Cubes

	An end-to-end toolkit for land use and land cover classification
    using big Earth observation data, based on machine learning methods 
    applied to satellite image data cubes, as described in Simoes et al (2021) <doi:10.3390/rs13132428>.
    Builds regular data cubes from collections in AWS, Microsoft Planetary Computer, 
    Brazil Data Cube, and Digital Earth Africa using the Spatio-temporal Asset Catalog (STAC) 
    protocol (<https://stacspec.org/> and the 'gdalcubes' R package 
    developed by Appel and Pebesma (2019) <doi:10.3390/data4030092>.
    Supports visualization methods for images and time series and 
    smoothing filters for dealing with noisy time series.
    Includes functions for quality assessment of training samples using self-organized maps 
    as presented by Santos et al (2021) <doi:10.1016/j.isprsjprs.2021.04.014>. 
    Provides machine learning methods including support vector machines, 
    random forests, extreme gradient boosting, multi-layer perceptrons,
    temporal convolutional neural networks proposed by Pelletier et al (2019) <doi:10.3390/rs11050523>, 
    residual networks by Fawaz et al (2019) <doi:10.1007/s10618-019-00619-1>, and temporal attention encoders
    by Garnot and Landrieu (2020) <arXiv:2007.00586>.
    Performs efficient classification of big Earth observation data cubes and includes 
    functions for post-classification smoothing based on Bayesian inference, and 
    methods for uncertainty assessment. Enables best
    practices for estimating area and assessing accuracy of land change as 
    recommended by Olofsson et al (2014) <doi:10.1016/j.rse.2014.02.015>.
    Minimum recommended requirements: 16 GB RAM and 4 CPU dual-core.
	"""
	
	homepage = "https://github.com/e-sensing/sits/"
	cran = "sits" 

	version("1.4.2-1", md5="af889f2e8d0a1d9d441f987a56c66b90")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-gdalutilities", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rstac@0.9.2.5:", type=("build", "run"))
	depends_on("r-sf@1.0.12:", type=("build", "run"))
	depends_on("r-showtext", type=("build", "run"))
	depends_on("r-sysfonts", type=("build", "run"))
	depends_on("r-slider@0.2:", type=("build", "run"))
	depends_on("r-terra@1.5.17:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-torch@0.11:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
