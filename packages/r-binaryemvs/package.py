# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinaryemvs(RPackage):
	"""Variable Selection for Binary Data Using the EM Algorithm

	Implements variable selection for high dimensional datasets with a binary response
    variable using the EM algorithm.  Both probit and logit models are supported.  Also included 
    is a useful function to generate high dimensional data with correlated variables.
	"""
	
	cran = "BinaryEMVS" 

	version("0.1", md5="dfdfd9b0830b43ce153b627a7d8469dc")

	depends_on("r@3.1.3:", type=("build", "run"))
