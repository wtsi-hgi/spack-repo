# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelsurv(RPackage):
	"""Relative Survival

	Contains functions for analysing relative survival data, including nonparametric estimators of net (marginal relative) survival, relative survival ratio, crude mortality, methods for fitting  and checking additive and multiplicative regression models, transformation approach, methods for dealing with population mortality tables. Work has been described in Pohar Perme, Pavlic (2018) <doi:10.18637/jss.v087.i08>.
	"""
	
	cran = "relsurv" 

	version("2.2-9", md5="ae6aef6358fa3f5de7e6b06915fa67d7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival@2.42:", type=("build", "run"))
	depends_on("r-date", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pammtools", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
