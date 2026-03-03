# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoisbinord(RPackage):
	"""Data Generation with Poisson, Binary and Ordinal Components

	Generation of multiple count, binary and ordinal variables simultaneously 
             given the marginal characteristics and association structure. Throughout the package,
             the word 'Poisson' is used to imply count data under the assumption of Poisson distribution. The details of the method are explained in Amatya, A. and Demirtas, H. (2015) <DOI:10.1080/00949655.2014.953534>.
	"""
	
	cran = "PoisBinOrd" 

	version("1.4.3", md5="b352bcec3881c7fbfea37ebca618396d")

	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-genord", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
