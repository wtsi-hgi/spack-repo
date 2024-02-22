# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbyx(RPackage):
	"""Inference for the Stress-Strength Model R = P(Y<X)

	Confidence intervals and point estimation for R under various parametric model assumptions; likelihood inference based on classical first-order approximations and higher-order asymptotic procedures.
	"""
	
	cran = "ProbYX" 

	version("1.1-0.1", md5="6ad40dae153a236038092ceda2bdcabd")

	depends_on("r@3.0.0:", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
