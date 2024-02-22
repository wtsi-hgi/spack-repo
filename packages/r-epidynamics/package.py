# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpidynamics(RPackage):
	"""Dynamic Models in Epidemiology

	Mathematical models of infectious diseases in humans and animals.
    Both, deterministic and stochastic models can be simulated and plotted.
	"""
	
	homepage = "https://github.com/oswaldosantos/EpiDynamics"
	cran = "EpiDynamics" 

	version("0.3.1", md5="1a2cdab34a7035c330438d4e57ff3828")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
