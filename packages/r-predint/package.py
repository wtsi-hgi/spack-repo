# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredint(RPackage):
	"""Prediction Intervals

	An implementation of prediction intervals for overdispersed count data,
            for overdispersed binomial data and for linear random effects models.
	"""
	
	homepage = "https://github.com/MaxMenssen/predint"
	cran = "predint" 

	version("2.2.1", md5="5918c45394e343192668001c58310784")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
