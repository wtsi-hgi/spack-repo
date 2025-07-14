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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/TimerQuant_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/TimerQuant/TimerQuant_1.32.0.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="9bf0b0b20f8d50043e3eee745a92005f53801df149f1297224953bee531754a2")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))

