# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGccfactor(RPackage):
	"""GCC Estimation of the Multilevel Factor Model

	Provides methods for model selection, estimation, bootstrap inference, and simulation for the 
    multilevel factor model, based on the principal component estimation and generalised 
    canonical correlation approach. Details can be found in "Generalised Canonical Correlation 
    Estimation of the Multilevel Factor Model." Lin and Shin (2023) <doi:10.2139/ssrn.4295429>.
	"""
	
	cran = "GCCfactor" 

	version("1.0.1", md5="20f2195d7fbe5ede7715460bbdc58a4a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
