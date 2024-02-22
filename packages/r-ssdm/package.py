# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsdm(RPackage):
	"""Stacked Species Distribution Modelling

	Allows to map species richness and endemism based on stacked
    species distribution models (SSDM). Individuals SDMs can be created using a
    single or multiple algorithms (ensemble SDMs). For each species, an SDM can
    yield a habitat suitability map, a binary map, a between-algorithm variance
    map, and can assess variable importance, algorithm accuracy, and between-
    algorithm correlation. Methods to stack individual SDMs include summing
    individual probabilities and thresholding then summing. Thresholding can be
    based on a specific evaluation metric or by drawing repeatedly from a Bernoulli
    distribution. The SSDM package also provides a user-friendly interface.
	"""
	
	homepage = "https://github.com/sylvainschmitt/SSDM"
	cran = "SSDM" 

	version("0.2.9", md5="5b9818cd0bdc04f275f28ae87d857aa1")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-sf@1.0.14:", type=("build", "run"))
	depends_on("r-raster@2.9.5:", type=("build", "run"))
	depends_on("r-mgcv@1.8.7:", type=("build", "run"))
	depends_on("r-earth@4.4.3:", type=("build", "run"))
	depends_on("r-rpart@4.1.10:", type=("build", "run"))
	depends_on("r-gbm@2.1.1:", type=("build", "run"))
	depends_on("r-randomforest@4.6.10:", type=("build", "run"))
	depends_on("r-dismo@1.0.12:", type=("build", "run"))
	depends_on("r-nnet@7.3.10:", type=("build", "run"))
	depends_on("r-e1071@1.6.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-shiny@0.12.2:", type=("build", "run"))
	depends_on("r-shinydashboard@0.5.1:", type=("build", "run"))
	depends_on("r-spthin@0.1:", type=("build", "run"))
	depends_on("r-poibin@1.3:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-doparallel@1.0.14:", type=("build", "run"))
	depends_on("r-iterators@1.0.10:", type=("build", "run"))
	depends_on("r-itertools@0.1.3:", type=("build", "run"))
	depends_on("r-leaflet@2.2:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-sdm@1.1.8:", type=("build", "run"))
