# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDreamer(RPackage):
	"""Dose Response Models for Bayesian Model Averaging

	Fits (longitudinal) dose-response models utilizing a Bayesian model
  averaging approach as outlined in Gould (2019) <doi:10.1002/bimj.201700211>
  for both continuous and binary responses.  Functions
  for plotting and calculating various posterior quantities
  (e.g. posterior mean, quantiles, probability of minimum efficacious dose,
  etc.) are also implemented.  Copyright Eli Lilly and Company (2019).
	"""
	
	homepage = "https://github.com/rich-payne/dreamer"
	cran = "dreamer" 

	version("3.1.0", md5="1563220bb8ded47a0c52c3cd94503ff7")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ellipsis@0.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-rjags@4.8:", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
