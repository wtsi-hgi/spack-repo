# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErcv(RPackage):
	"""Fitting Tails by the Empirical Residual Coefficient of Variation

	Provides a methodology simple and trustworthy for the analysis of extreme values and multiple threshold tests for a generalized Pareto distribution, together
    with an automatic threshold selection algorithm. See del Castillo, J, Daoudi, J and Lockhart, R (2014) <doi:10.1111/sjos.12037>.
	"""
	
	cran = "ercv" 

	version("1.0.1", md5="7d50dad3bfe6ff1933d7e8019e28bfc5")

	depends_on("r@3.5:", type=("build", "run"))
