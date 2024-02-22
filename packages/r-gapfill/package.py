# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGapfill(RPackage):
	"""Fill Missing Values in Satellite Data

	Tools to fill missing values in satellite data and to develop new
    gap-fill algorithms. The methods are tailored to data (images) observed
    at equally-spaced points in time. The package is illustrated with MODIS
    NDVI data.
	"""
	
	homepage = "https://github.com/florafauna/gapfill"
	cran = "gapfill" 

	version("0.9.6-1", md5="0bf2b2af120a89c9210c0c0ee85dc835")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-foreach@1.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-quantreg@5:", type=("build", "run"))
