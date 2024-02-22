# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmawgen(RPackage):
	"""Multi-Site Auto-Regressive Weather GENerator

	S3 and S4 functions are implemented for spatial multi-site
    stochastic generation of daily time series of temperature and
    precipitation. These tools make use of Vector AutoRegressive models (VARs).
    The weather generator model is then saved as an object and is calibrated by
    daily instrumental "Gaussianized" time series through the 'vars' package
    tools. Once obtained this model, it can it can be used for weather
    generations and be adapted to work with several climatic monthly time
    series.
	"""
	
	homepage = "https://github.com/ecor/RMAWGEN"
	cran = "RMAWGEN" 

	version("1.3.7", md5="ccea7f279f22c506a1aebb36442623c2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-date", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
