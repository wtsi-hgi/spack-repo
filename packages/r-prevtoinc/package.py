# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrevtoinc(RPackage):
	"""Prevalence to Incidence Calculations for Point-Prevalence
Studies in a Nosocomial Setting

	Functions to simulate point prevalence studies (PPSs) of healthcare-associated infections (HAIs) and to convert prevalence to incidence in steady state setups. 
    Companion package to the preprint Willrich et al., From prevalence to incidence - a new approach in the hospital setting;
    <doi:10.1101/554725> , where methods are explained in detail.
	"""
	
	cran = "prevtoinc" 

	version("0.12.0", md5="1baddd8d9ba570a956cb3e435d5601b6")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
