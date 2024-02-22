# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMqmf(RPackage):
	"""Modelling and Quantitative Methods in Fisheries

	Complements the book 
    "Using R for Modelling and Quantitative Methods in Fisheries"
    ISBN 9780367469894, published in 
    2021 by Chapman & Hall in their "Using R series". 
    There are numerous functions and data-sets that are used in the 
    book's many practical examples. 
	"""
	
	homepage = "https://github.com/haddonm/MQMF/"
	cran = "MQMF" 

	version("0.1.5", md5="5fd07260b52731bc77e00307b637192b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
