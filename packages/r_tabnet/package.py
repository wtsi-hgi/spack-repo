# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabnet(RPackage):
	"""Fit 'TabNet' Models for Classification and Regression

	Implements the 'TabNet' model by Sercan O. Arik et al. (2019) <arXiv:1908.07442> 
    with 'Coherent Hierarchical Multi-label Classification Networks' by Giunchiglia et al.
    <arXiv:2010.10151> and provides a consistent interface for fitting and creating 
    predictions. It's also fully compatible with the 'tidymodels' ecosystem.
	"""
	
	homepage = "https://mlverse.github.io/tabnet/"
	cran = "tabnet" 

	version("0.5.0", md5="10a60aa94917666c6e384a653f3e979e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-torch@0.4:", type=("build", "run"))
	depends_on("r-hardhat@1.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-coro", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
