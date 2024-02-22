# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmea(RPackage):
	"""Synchrony in Motion Energy Analysis (MEA) Time-Series

	A suite of tools useful to read, visualize and export bivariate motion energy time-series. Lagged synchrony between subjects can be analyzed through windowed cross-correlation. Surrogate data generation allows an estimation of pseudosynchrony that helps to estimate the effect size of the observed synchronization. Kleinbub, J. R., & Ramseyer, F. T. (2020). rMEA: An R package to assess nonverbal synchronization in motion energy analysis time-series. Psychotherapy research, 1-14. <doi:10.1080/10503307.2020.1844334>.
	"""
	
	homepage = "https://github.com/kleinbub/rMEA"
	cran = "rMEA" 

	version("1.2.2", md5="2382f9524c911a3e17fd776eb3e409e4")

	depends_on("r@4:", type=("build", "run"))
