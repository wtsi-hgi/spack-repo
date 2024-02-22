# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReslr(RPackage):
	"""Modelling Relative Sea Level Data

	The Bayesian modelling of relative sea-level data
    using a comprehensive approach that incorporates
    various statistical models within a unifying framework. 
    Details regarding each statistical models; 
    linear regression (Ashe et al 2019) <doi:10.1016/j.quascirev.2018.10.032>, 
    change point models (Cahill et al 2015) <doi:10.1088/1748-9326/10/8/084002>, 
    integrated Gaussian process models (Cahill et al 2015) <doi:10.1214/15-AOAS824>, 
    temporal splines (Upton et al 2023) <arXiv:2301.09556>, 
    spatio-temporal splines (Upton et al 2023) <arXiv:2301.09556> and
    generalised additive models (Upton et al 2023) <arXiv:2301.09556>.
    This package facilitates data loading, 
    model fitting and result summarisation.
    Notably, it accommodates the inherent measurement errors
    found in relative sea-level data across multiple dimensions,
    allowing for their inclusion in the statistical models.
	"""
	
	homepage = "https://github.com/maeveupton/reslr"
	cran = "reslr" 

	version("0.1.1", md5="6c47f67cae5a87a444af7ddf7d89e482")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidybayes", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
