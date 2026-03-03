# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPln(RPackage):
	"""Polytomous Logit-Normit (Graded Logistic) Model Estimation

	Performs bivariate composite likelihood and full
        information maximum likelihood estimation for polytomous
        logit-normit (graded logistic) item response theory (IRT)
        models.
	"""
	
	cran = "pln" 

	version("0.2-2", md5="560785e153d4086fff7c7dc5ee28c58f")

	depends_on("r@2.9:", type=("build", "run"))
