# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVandalico(RPackage):
	"""Evaluation of Presence-Absence Models

	Collection of functions to evaluate presence-absence models. The 
    main function corrects discrimination for the representativeness effect 
    following: 
    Jiménez-Valverde (2022) "The uniform AUC: dealing with the 
    representativeness effect in presence-absence models. Methods Ecol. Evol, 
    accepted on 28 January 2022.
	"""
	
	cran = "vandalico" 

	version("0.0.1", md5="558d787008951a7546de49e4da0c2eb1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rocr@1.0.7:", type=("build", "run"))
