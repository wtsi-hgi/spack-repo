# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnovir(RPackage):
	"""Analysis of Virulence

	Epidemiological population dynamics models traditionally define 
    a pathogen's virulence as the increase in the per capita rate of mortality 
    of infected hosts due to infection. This package provides functions 
    allowing virulence to be estimated by maximum likelihood techniques. The 
    approach is based on the analysis of relative survival comparing survival 
    in matching cohorts of infected vs. uninfected hosts (Agnew 2019) 
    <doi:10.1101/530709>. 
	"""
	
	homepage = "https://www.biorxiv.org/content/10.1101/530709v1"
	cran = "anovir" 

	version("0.1.0", md5="4a7e2cc57de16aa7fe00e15f3e0f3dc7")

	depends_on("r-bbmle", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
