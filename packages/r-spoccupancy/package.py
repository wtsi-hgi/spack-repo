# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpoccupancy(RPackage):
	"""Single-Species, Multi-Species, and Integrated Spatial Occupancy
Models

	Fits single-species, multi-species, and integrated non-spatial and spatial occupancy models using Markov Chain Monte Carlo (MCMC). Models are fit using Polya-Gamma data augmentation detailed in Polson, Scott, and Windle (2013) <doi:10.1080/01621459.2013.829001>. Spatial models are fit using either Gaussian processes or Nearest Neighbor Gaussian Processes (NNGP) for large spatial datasets. Details on NNGP models are given in Datta, Banerjee, Finley, and Gelfand (2016) <doi:10.1080/01621459.2015.1044091> and Finley, Datta, and Banerjee (2020) <arXiv:2001.09111>. Provides functionality for data integration of multiple single-species occupancy data sets using a joint likelihood framework. Details on data integration are given in Miller, Pacifici, Sanderlin, and Reich (2019) <doi:10.1111/2041-210X.13110>. Details on single-species and multi-species models are found in MacKenzie, Nichols, Lachman, Droege, Royle, and Langtimm (2002) <doi:10.1890/0012-9658(2002)083[2248:ESORWD]2.0.CO;2> and Dorazio and Royle <doi:10.1198/016214505000000015>, respectively. 
	"""
	
	homepage = "https://www.jeffdoser.com/files/spoccupancy-web"
	cran = "spOccupancy" 

	version("0.7.3", md5="979428aa11ff4e4129a104495f3c5e72")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-spabundance", type=("build", "run"))
