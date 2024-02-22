# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLvnet(RPackage):
	"""Latent Variable Network Modeling

	Estimate, fit and compare Structural Equation Models (SEM) and network models (Gaussian Graphical Models; GGM) using OpenMx. Allows for two possible generalizations to include GGMs in SEM: GGMs can be used between latent variables (latent network modeling; LNM) or between residuals (residual network modeling; RNM). For details, see Epskamp, Rhemtulla and Borsboom (2017) <doi:10.1007/s11336-017-9557-x>.
	"""
	
	cran = "lvnet" 

	version("0.3.5", md5="dcd562aaab56e10093e4d7f6dac1b77c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-openmx", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-semplot", type=("build", "run"))
