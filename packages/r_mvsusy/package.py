# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvsusy(RPackage):
	"""Multivariate Surrogate Synchrony

	Multivariate Surrogate Synchrony ('mvSUSY') estimates the synchrony within datasets that contain more than two time series. 'mvSUSY' was developed from Surrogate Synchrony ('SUSY') with respect to implementing surrogate controls, and extends synchrony estimation to multivariate data. 'mvSUSY' works as described in Meier & Tschacher (2021).
	"""
	
	homepage = "https://wtschacher.github.io/mvSUSY/"
	cran = "mvSUSY" 

	version("0.1.0", md5="7d0b6cfd3024444d90231905ca57e7d7")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcppalgos", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
