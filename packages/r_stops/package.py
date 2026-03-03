# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStops(RPackage):
	"""Structure Optimized Proximity Scaling

	A collection of methods that fit nonlinear distance transformations in multidimensional scaling (MDS) and trade-off the fit with structure considerations to find optimal parameters also known as structure optimized proximity scaling (STOPS) (Rusch, Mair & Hornik, 2023,<doi:10.1007/s11222-022-10197-w>). The package contains various functions, wrappers, methods and classes for fitting, plotting and displaying different MDS models in a STOPS framework like Torgerson (classical) scaling, scaling by majorizing a complex function (SMACOF), Sammon mapping, elastic scaling, symmetric SMACOF, spherical SMACOF, s-stress, r-stress, power MDS, power elastic scaling, power Sammon mapping, power stress MDS (POST-MDS), approximate power stress, Box-Cox MDS, local MDS and Isomap. All of these models can also be fit individually with given hyperparameters or by optimizing over hyperparameters based on fit only (i.e., no structure considerations). The package further contains functions for optimization, specifically the adaptive Luus-Jaakola algorithm and a wrapper for Bayesian optimization with treed Gaussian process with jumps to linear models, and functions for various c-structuredness indices.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/stops/"
	cran = "stops" 

	version("1.0-1", md5="4e6819172c3a4aa983607392cb69e4ce")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-smacof", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-cordillera", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pso", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-acepack", type=("build", "run"))
	depends_on("r-minerva", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-diceoptim", type=("build", "run"))
	depends_on("r-dicekriging", type=("build", "run"))
	depends_on("r-tgp", type=("build", "run"))
	depends_on("r-pomp", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-scagnostics", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-cmaes", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
