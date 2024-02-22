# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGen3sis(RPackage):
	"""General Engine for Eco-Evolutionary Simulations

	Contains an engine for spatially-explicit eco-evolutionary mechanistic models with a modular implementation and several support functions. It allows exploring the consequences of ecological and macroevolutionary processes across realistic or theoretical spatio-temporal landscapes on biodiversity patterns as a general term. Reference: Oskar Hagen, Benjamin Flueck, Fabian Fopp, Juliano S. Cabral, Florian Hartig, Mikael Pontarp, Thiago F. Rangel, Loic Pellissier (2021) "gen3sis: A general engine for eco-evolutionary simulations of the processes that shape Earth's biodiversity" <doi:10.1371/journal.pbio.3001340>.
	"""
	
	homepage = "https://github.com/project-Gen3sis/R-package"
	cran = "gen3sis" 

	version("1.5.11", md5="1cffe18bdce984bae2e2d5eee8861dcd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-gdistance", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
