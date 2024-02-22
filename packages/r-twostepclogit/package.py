# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwostepclogit(RPackage):
	"""Conditional Logistic Regression: A Two-Step Estimation Method

	Conditional logistic regression with longitudinal follow up and
    individual-level random coefficients: A stable and efficient
    two-step estimation method.
	"""
	
	cran = "TwoStepCLogit" 

	version("1.2.5", md5="8600f9dd62c22c1900c37c3bd68d055b")

	depends_on("r-survival", type=("build", "run"))
