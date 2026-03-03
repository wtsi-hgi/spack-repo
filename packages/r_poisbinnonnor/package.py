# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoisbinnonnor(RPackage):
	"""Data Generation with Poisson, Binary and Continuous Components

	Generation of multiple count, binary and continuous variables simultaneously 
             given the marginal characteristics and association structure. Throughout the package,
             the word 'Poisson' is used to imply count data under the assumption of Poisson distribution. 
             The details of the method are explained in Amatya et al. (2015) <DOI:10.1080/00949655.2014.953534>.
	"""
	
	cran = "PoisBinNonNor" 

	version("1.3.3", md5="681d7548de76b90f42c4de9ab59092b6")

	depends_on("r-bb", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
