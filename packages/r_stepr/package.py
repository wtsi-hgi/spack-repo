# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepr(RPackage):
	"""Multiscale Change-Point Inference

	Allows fitting of step-functions to univariate serial data where neither the number of jumps nor their positions is known by implementing the multiscale regression estimators SMUCE, simulataneous multiscale changepoint estimator, (K. Frick, A. Munk and H. Sieling, 2014) <doi:10.1111/rssb.12047> and HSMUCE, heterogeneous SMUCE, (F. Pein, H. Sieling and A. Munk, 2017) <doi:10.1111/rssb.12202>. In addition, confidence intervals for the change-point locations and bands for the unknown signal can be obtained.
	"""
	
	cran = "stepR" 

	version("2.1-9", md5="04e1eea6c1a6a43bae9beba6c6ff1c3b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lowpassfilter@1:", type=("build", "run"))
	depends_on("r-r-cache@0.10:", type=("build", "run"))
	depends_on("r-digest@0.6.10:", type=("build", "run"))
