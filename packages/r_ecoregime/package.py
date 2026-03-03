# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcoregime(RPackage):
	"""Analysis of Ecological Dynamic Regimes

	A toolbox for implementing the Ecological Dynamic Regime framework 
    (Sánchez-Pinillos et al., 2023 <doi:10.1002/ecm.1589>) to 
    characterize and compare groups of ecological trajectories in multidimensional 
    spaces defined by state variables. The package includes the RETRA-EDR algorithm 
    to identify representative trajectories, functions to generate, summarize, 
    and visualize representative trajectories, and several metrics to quantify 
    the distribution and heterogeneity of trajectories in an ecological dynamic 
    regime and quantify the dissimilarity between two or more ecological dynamic 
    regimes.
	"""
	
	homepage = "https://mspinillos.github.io/ecoregime/"
	cran = "ecoregime" 

	version("0.1.3", md5="21edf1c2d92589c674abc3f1b75ba914")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ecotraj", type=("build", "run"))
	depends_on("r-gdatools", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-smacof", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
