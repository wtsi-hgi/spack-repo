# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmcfun(RPackage):
	"""Diffusion Model of Conflict (DMC) in Reaction Time Tasks

	
  DMC model simulation detailed in Ulrich, R., Schroeter, H., Leuthold, H., & Birngruber, T. (2015).
  Automatic and controlled stimulus processing in conflict tasks: Superimposed diffusion processes and delta functions.
  Cognitive Psychology, 78, 148-174. Ulrich et al. (2015) <doi:10.1016/j.cogpsych.2015.02.005>.
  Decision processes within choice reaction-time (CRT) tasks are often modelled using evidence accumulation models (EAMs),
  a variation of which is the Diffusion Decision Model (DDM, for a review, see Ratcliff & McKoon, 2008).
  Ulrich et al. (2015) introduced a Diffusion Model for Conflict tasks (DMC). The DMC model combines common
  features from within standard diffusion models with the addition of superimposed controlled and automatic activation.
  The DMC model is used to explain distributional reaction time (and error rate) patterns in common behavioural
  conflict-like tasks (e.g., Flanker task, Simon task). This R-package implements the DMC model and provides functionality
  to fit the model to observed data. Further details are provided in the following paper: 
  Mackenzie, I.G., & Dudschig, C. (2021). DMCfun: An R package for fitting Diffusion Model of Conflict (DMC) to reaction 
  time and error rate data. Methods in Psychology, 100074. <doi:10.1016/j.metip.2021.100074>.
	"""
	
	homepage = "https://github.com/igmmgi/DMCfun"
	cran = "DMCfun" 

	version("3.5.4", md5="3f08cd3ab196b1f9b70d0487a35bd0e1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
