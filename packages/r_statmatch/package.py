# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatmatch(RPackage):
	"""Statistical Matching or Data Fusion

	Integration of two data sources referred to the same target population which share a number of variables. Some functions can also be used to impute missing values in data sets through hot deck imputation methods. Methods to perform statistical matching when dealing  with data from complex sample surveys are available too.
	"""
	
	homepage = "https://github.com/marcellodo/StatMatch"
	cran = "StatMatch" 

	version("1.4.1", md5="cfed43a698cc7b9dcd36e6fc67cd6bf4")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
