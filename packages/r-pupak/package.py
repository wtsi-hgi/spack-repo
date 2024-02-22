# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPupak(RPackage):
	"""Parameter Estimation, and Plot Visualization of Adsorption
Kinetic Models

	Contains model fitting functions for linear and non-linear adsorption kinetic and diffusion models. Adsorption kinetics is used for characterizing the rate of solute adsorption and the time necessary for the adsorption process. Adsorption kinetics offers vital information on adsorption rate, adsorbent performance in response time, and mass transfer processes. In addition, diffusion models are included in the package as solute diffusion affects the adsorption kinetic experiments. This package consists of 20 adsorption and diffusion models, including Pseudo First Order (PFO), Pseudo Second Order (PSO), Elovich, and Weber-Morris model (commonly called the intraparticle model) stated by Plazinski et al. (2009) <doi:10.1016/j.cis.2009.07.009>. This package also contains a summary function where the statistical errors of each model are ranked for a more straightforward determination of the best fit model.
	"""
	
	cran = "PUPAK" 

	version("0.1.1", md5="90eec6ff10d3d4d229e883dd0d82d783")

	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nls2", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
