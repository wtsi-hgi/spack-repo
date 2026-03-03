# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeuromplex(RPackage):
	"""Neural Multiplexing Analysis

	Statistical methods for whole-trial and time-domain analysis of single cell neural response to multiple stimuli presented simultaneously. The package is based on the paper by C Glynn, ST Tokdar, A Zaman, VC Caruso, JT Mohl, SM Willett, and JM Groh (2021) "Analyzing second order stochasticity of neural spiking under stimuli-bundle exposure", is in press for publication by the Annals of Applied Statistics. A preprint may be found at <arXiv:1911.04387>.
	"""
	
	cran = "neuromplex" 

	version("1.0-1", md5="dc18fe1ebde0f53847222321706f0d0b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayeslogit", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
