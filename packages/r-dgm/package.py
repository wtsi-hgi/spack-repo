# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDgm(RPackage):
	"""Dynamic Graphical Models

	
    Dynamic graphical models for multivariate time series data to estimate directed
    dynamic networks in functional magnetic resonance imaging (fMRI), see Schwab et
    al. (2017) <doi:10.1016/j.neuroimage.2018.03.074>.
	"""
	
	homepage = "https://github.com/schw4b/DGM"
	cran = "DGM" 

	version("1.7.4", md5="2c3b67b76927db44c7f0a165c3a4fdfa")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-coin@1.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
