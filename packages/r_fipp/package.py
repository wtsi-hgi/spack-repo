# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFipp(RPackage):
	"""Induced Priors in Bayesian Mixture Models

	Computes implicitly induced quantities from prior/hyperparameter    
    specifications of three Mixtures of Finite Mixtures models: Dirichlet 
    Process Mixtures (DPMs; Escobar and West (1995) 
    <doi:10.1080/01621459.1995.10476550>), Static Mixtures of Finite Mixtures 
    (Static MFMs; Miller and Harrison (2018) 
    <doi:10.1080/01621459.2016.1255636>), and Dynamic Mixtures of Finite 
    Mixtures (Dynamic MFMs; Frühwirth-Schnatter, Malsiner-Walli and Grün (2020)
    <arXiv:2005.09918>). For methodological details, please refer to 
    Greve, Grün, Malsiner-Walli and Frühwirth-Schnatter (2020)
    <arXiv:2012.12337>) as well as the package vignette.
	"""
	
	cran = "fipp" 

	version("1.0.0", md5="f69a09fbe140b628d054cb8520c6e496")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
