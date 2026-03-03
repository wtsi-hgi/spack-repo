# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvdesc(RPackage):
	"""Profiling Compliers and Non-Compliers for Instrumental Variable
Analysis

	Estimating the mean and variance of a covariate for the complier, never-taker and always-taker subpopulation in the context of instrumental variable estimation. This package implements the method described in Marbach and Hangartner (2020) <doi:10.1017/pan.2019.48> and Hangartner, Marbach, Henckel, Maathuis, Kelz and Keele (2021) <arXiv:2103.06328>.
	"""
	
	homepage = "https://github.com/sumtxt/ivdesc/"
	cran = "ivdesc" 

	version("1.1.1", md5="70bc626fafae60202c988c74ee2feb3d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-knitr@1.20.8:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-rsample@0.0.3:", type=("build", "run"))
