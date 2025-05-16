# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMplusautomation(RPackage):
	"""An R Package for Facilitating Large-Scale Latent Variable
Analyses in Mplus

	Leverages the R language to automate latent variable model estimation
	and interpretation using 'Mplus', a powerful latent variable modeling program
	developed by Muthen and Muthen (<https://www.statmodel.com>). Specifically, this package
    provides routines for creating related groups of models, running batches of
    models, and extracting and tabulating model parameters and fit statistics.
	"""
	
	homepage = "https://michaelhallquist.github.io/MplusAutomation/"
	cran = "MplusAutomation" 

	version("1.1.1", md5="75c74a7c133d044af04a51ab298024cc")
	version("1.1.0", md5="e3fbf9652949fd9f5fcce37f3b43cf7e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gsubfn", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-texreg", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
