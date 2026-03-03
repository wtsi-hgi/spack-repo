# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForeca(RPackage):
	"""Forecastable Component Analysis

	Implementation of Forecastable Component Analysis ('ForeCA'),
    including main algorithms and auxiliary function (summary, plotting, etc.) to
    apply 'ForeCA' to multivariate time series data. 'ForeCA' is a novel dimension
    reduction (DR) technique for temporally dependent signals. Contrary to other
    popular DR methods, such as 'PCA' or 'ICA', 'ForeCA' takes time dependency
    explicitly into account and searches for the most ''forecastable'' signal.
    The measure of forecastability is based on the Shannon entropy of the spectral
    density of the transformed signal.
	"""
	
	homepage = "https://github.com/gmgeorg/ForeCA"
	cran = "ForeCA" 

	version("0.2.7", md5="74d16344854df9dd29399a54f45da453")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-astsa@1.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
