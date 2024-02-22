# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDosefinding(RPackage):
	"""Planning and Analyzing Dose Finding Experiments

	The DoseFinding package provides functions for the design and analysis
	     of dose-finding experiments (with focus on pharmaceutical Phase
	     II clinical trials). It provides functions for: multiple contrast
	     tests, fitting non-linear dose-response models (using Bayesian and
	     non-Bayesian estimation), calculating optimal designs and an
	     implementation of the MCPMod methodology (Pinheiro et al. (2014)
	     <doi:10.1002/sim.6052>).
	"""
	
	cran = "DoseFinding" 

	version("1.1-1", md5="22e563ae0fd7276fdbee7c063d76166f")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r@2.15:", type=("build", "run"))
