# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMblm(RPackage):
	"""Median-Based Linear Models

	Provides linear models based on Theil-Sen
        single median and Siegel repeated medians. They are very robust
        (29 or 50 percent breakdown point, respectively), and if no
        outliers are present, the estimators are very similar to OLS.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "mblm" 

	version("0.12.1", md5="c3cc076c394b75fd8fc081a3fef4a2fb")

