# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetchain(RPackage):
	"""Inferring Causal Effects on Collective Outcomes under
Interference

	In networks, treatments may spill over from the treated individual to his or her social contacts and outcomes may be contagious over time. Under this setting, causal inference on the collective outcome observed over all network is often of interest. We use chain graph models approximating the projection of the full longitudinal data onto the observed data to identify the causal effect of the intervention on the whole outcome. Justification of such approximation is demonstrated in Ogburn et al. (2018) <arXiv:1812.04990>.
	"""
	
	cran = "netchain" 

	version("0.2.0", md5="9d536db46071eef2298b042071c2107a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
