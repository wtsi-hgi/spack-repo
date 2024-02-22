# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaccadr(RPackage):
	"""Extract Saccades via an Ensemble of Methods Approach

	A modular and extendable approach to extract (micro)saccades from gaze samples via an ensemble of methods.
  Although there is an agreement about a general definition of a saccade, the more specific details are harder to agree upon.
  Therefore, there are numerous algorithms that extract saccades based on various heuristics, which differ in the assumptions about velocity,
  acceleration, etc. The package uses three methods (Engbert and Kliegl (2003) <doi:10.1016/S0042-6989(03)00084-1>,
  Otero-Millan et al. (2014)<doi:10.1167/14.2.18>, and Nyström and Holmqvist (2010) <doi:10.3758/BRM.42.1.188>)
  to label individual samples and then applies a majority vote approach to identify saccades. The package includes three
  methods but can be extended via custom functions. It also uses a modular approach to compute velocity and
  acceleration from noisy samples. Finally, you can obtain methods votes per gaze sample instead of saccades.
	"""
	
	homepage = "https://github.com/alexander-pastukhov/saccadr/"
	cran = "saccadr" 

	version("0.1.3", md5="418d2a6252f6e51eda46d637175444c1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
