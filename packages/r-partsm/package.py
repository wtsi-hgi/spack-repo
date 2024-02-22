# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartsm(RPackage):
	"""Periodic Autoregressive Time Series Models

	Basic functions to fit and predict periodic autoregressive time series models. These models are discussed in the book P.H. Franses (1996) "Periodicity and Stochastic Trends in Economic Time Series", Oxford University Press. Data set analyzed in that book is also provided. NOTE: the package was orphaned during several years. It is now only maintained, but no major enhancements are expected, and the maintainer cannot provide any support. 
	"""
	
	homepage = "https://github.com/MatthieuStigler/partsm"
	cran = "partsm" 

	version("1.1-3", md5="735f1da543935b7a51f2140e71b40e3e")

	depends_on("r@2.14:", type=("build", "run"))
