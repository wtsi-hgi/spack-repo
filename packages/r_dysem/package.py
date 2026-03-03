# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDysem(RPackage):
	"""Dyadic Structural Equation Modeling

	Scripting of structural equation models via 'lavaan' for
    Dyadic Data Analysis, and helper functions for supplemental
    calculations, tabling, and model visualization.  Current models
    supported include Dyadic Confirmatory Factor Analysis, the Actor–Partner 
    Interdependence Model (observed and latent), the Common Fate Model
    (observed and latent), Mutual Influence Model (latent), and the Bifactor
    Dyadic Model (latent).
	"""
	
	homepage = "https://github.com/jsakaluk/dySEM"
	cran = "dySEM" 

	version("1.0.0", md5="26dbdf1d7fe27c1e7f47d4be078a8941")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-semplot", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
