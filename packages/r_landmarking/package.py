# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLandmarking(RPackage):
	"""Analysis using Landmark Models

	The landmark approach allows survival predictions to be
	updated dynamically as new measurements from an individual are recorded.
	The idea is to set predefined time points, known as "landmark times",
	and form a model at each landmark time using only the individuals in the
	risk set. This package allows the longitudinal data to be modelled
	either using the last observation carried forward or linear mixed
	effects modelling. There is also the option to model competing risks,
	either through cause-specific Cox regression or Fine-Gray regression.
	To find out more about the methods in this package, please see 
	<https://isobelbarrott.github.io/Landmarking/articles/Landmarking>.
	"""
	
	homepage = "https://github.com/isobelbarrott/Landmarking/"
	cran = "Landmarking" 

	version("1.0.0", md5="f064977eed908f5ffa90f12798bb891a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-riskregression", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pec", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mstate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
