# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimerquant(RPackage):
	"""Timer Quantification

	Supplementary Data package for tandem timer methods paper by Barry et al. (2015) including TimerQuant shiny applications.
	"""
	
	bioc = "TimerQuant"

	version("1.38.0", commit="b916b219459c312fb43aeb3a16de39aa906c94f3")
	version("1.32.0", commit="ab5a87f633c567449c7a167356bc5b987e54b454")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))

