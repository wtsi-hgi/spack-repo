# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGastempt(RPackage):
	"""Analyzing Gastric Emptying from MRI or Scintigraphy

	Fits gastric emptying time series from MRI or 'scintigraphic' measurements
   using nonlinear mixed-model population fits with 'nlme' and Bayesian methods with 
   Stan; computes derived parameters such as t50 and AUC.
	"""
	
	homepage = "https://github.com/dmenne/gastempt"
	cran = "gastempt" 

	version("0.5.5", md5="df5a75b4365af8ab943adb8dcfeeb15e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcpp@1.0.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-rstan@2.21:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-utf8", type=("build", "run"))
	depends_on("r-stanheaders@2.21:", type=("build", "run"))
	depends_on("r-bh@1.72.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.7:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
