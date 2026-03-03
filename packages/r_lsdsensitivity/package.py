# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsdsensitivity(RPackage):
	"""Sensitivity Analysis Tools for LSD Simulations

	Tools for sensitivity analysis of LSD simulation models. Reads object-oriented data produced by LSD simulation models and performs screening and global sensitivity analysis (Sobol decomposition method, Saltelli et al. (2008) ISBN:9780470725177). A Kriging or polynomial meta-model (Kleijnen (2009) <doi:10.1016/j.ejor.2007.10.013>) is estimated using the simulation data to provide the data required by the Sobol decomposition. LSD (Laboratory for Simulation Development) is free software developed by Marco Valente and Marcelo C. Pereira (documentation and downloads available at <https://www.labsimdev.org/>).
	"""
	
	cran = "LSDsensitivity" 

	version("1.2.3", md5="b6cf2ae0615118edd9c03c701fcc2b38")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lsdinterface@1.2.1:", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-ksamples", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-lawstat", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-sensitivity", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-dicekriging", type=("build", "run"))
