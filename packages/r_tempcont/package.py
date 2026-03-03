# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTempcont(RPackage):
	"""Temporal Contributions on Trends using Mixed Models

	Method to estimate the effect of the trend in predictor variables on the observed trend
 of the response variable using mixed models with temporal autocorrelation. See Fernández-Martínez et
 al. (2017 and 2019) <doi:10.1038/s41598-017-08755-8> <doi:10.1038/s41558-018-0367-7>.
	"""
	
	homepage = "https://github.com/burriach/tempcont"
	cran = "TempCont" 

	version("0.1.0", md5="0edd0e564b98ec21dc59f7a0ab0eeb42")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
