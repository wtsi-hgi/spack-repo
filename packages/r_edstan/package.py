# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdstan(RPackage):
	"""Stan Models for Item Response Theory

	Provides convenience functions and pre-programmed Stan models
    related to item response theory. Its purpose is to make fitting
    common item response theory models using Stan easy.
	"""
	
	cran = "edstan" 

	version("1.0.6", md5="75c100e9ab24b5fa87fee7cf6c65ddd3")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rstan@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
