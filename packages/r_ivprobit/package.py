# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvprobit(RPackage):
	"""Instrumental Variables Probit Model

	Compute the instrumental variables probit model using  the Amemiya's Generalized Least Squares estimators (Amemiya, Takeshi, (1978) <doi: 10.2307/1911443>).
	"""
	
	cran = "ivprobit" 

	version("1.1", md5="6a0d01c7b044ad884b88814cf690713a")

	depends_on("r-formula", type=("build", "run"))
