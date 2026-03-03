# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPersonalized(RPackage):
	"""Estimation and Validation Methods for Subgroup Identification
and Personalized Medicine

	Provides functions for fitting and validation of models for subgroup
    identification and personalized medicine / precision medicine under the general subgroup
    identification framework of Chen et al. (2017) <doi:10.1111/biom.12676>.
    This package is intended for use for both randomized controlled trials and
    observational studies and is described in detail in Huling and Yu (2021) 
    <doi:10.18637/jss.v098.i05>.
	"""
	
	homepage = "https://jaredhuling.org/personalized/"
	cran = "personalized" 

	version("0.2.7", md5="0197701380cadf652582c993e3c7506a")

	depends_on("r-glmnet@2.0.13:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
