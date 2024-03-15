# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegdif(RPackage):
	"""Regularized Differential Item Functioning

	Performs regularization of differential item functioning (DIF) parameters 
    in item response theory (IRT) models (Belzak & Bauer, 2020)
    <https://pubmed.ncbi.nlm.nih.gov/31916799/> using a penalized expectation-maximization
    algorithm.
	"""
	
	cran = "regDIF" 

	version("1.1.1", md5="a94ea7d71591d53b775166c844c63b8d")

	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
