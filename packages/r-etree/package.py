# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtree(RPackage):
	"""Classification and Regression with Structured and Mixed-Type
Data

	Implementation of Energy Trees, a statistical model to perform 
    classification and regression with structured and mixed-type data. The
    model has a similar structure to Conditional Trees, but brings in Energy
    Statistics to test independence between variables that are possibly 
    structured and of different nature. Currently, the package covers functions
    and graphs as structured covariates. It builds upon 'partykit' to
    provide functionalities for fitting, printing, plotting, and predicting with
    Energy Trees. Energy Trees are described in Giubilei et al. (2022) 
    <arXiv:2207.04430>. 
	"""
	
	homepage = "https://github.com/ricgbl/etree"
	cran = "etree" 

	version("0.1.0", md5="d457ef91eddc369f26bc09626f6c5029")

	depends_on("r@3.7:", type=("build", "run"))
	depends_on("r-braingraph", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-fda-usc@2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-networkdistance", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tda", type=("build", "run"))
	depends_on("r-usedist", type=("build", "run"))
