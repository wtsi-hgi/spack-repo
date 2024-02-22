# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSephora(RPackage):
	"""Statistical Estimation of Phenological Parameters

	Provides functions and methods for estimating phenological dates (green up, 
  start of a season, maturity, senescence, end of a season and dormancy) from (nearly) 
  periodic Earth Observation time series. These dates are critical points of some 
  derivatives of an idealized curve which, in turn, is obtained through a functional principal 
  component analysis-based regression model. Some of the methods implemented here are 
  based on T. Krivobokova, P. Serra and F. Rosales (2022) <https://www.sciencedirect.com/science/article/pii/S0167947322000998>. 
  Methods for handling and plotting Earth observation time series are also provided.
	"""
	
	cran = "sephora" 

	version("0.1.31", md5="697bdecf6cd90e4f2f115e96bd449c7e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-geots@0.1.7:", type=("build", "run"))
	depends_on("r-ebsc@4.15:", type=("build", "run"))
	depends_on("r-rootsolve@1.8.2.3:", type=("build", "run"))
	depends_on("r-dtwclust@5.5.10:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-doparallel@1.0.14:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-nlme@3.1.157:", type=("build", "run"))
	depends_on("r-mass@7.3.57:", type=("build", "run"))
	depends_on("r-ggnewscale@0.4.7:", type=("build", "run"))
	depends_on("r-spiralize@1.0.6:", type=("build", "run"))
