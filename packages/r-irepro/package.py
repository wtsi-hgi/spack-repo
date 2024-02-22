# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrepro(RPackage):
	"""Reproducibility for Interval-Censored Data

	Calculates intraclass correlation coefficient (ICC) for assessing reproducibility of interval-censored data with two repeated measurements (Kovacic and Varnai (2014) <doi:10.1097/EDE.0000000000000139>). ICC is estimated by maximum likelihood from model with one fixed and one random effect (both intercepts). Help in model checking (normality of subjects' means and residuals) is provided.
	"""
	
	cran = "iRepro" 

	version("1.2", md5="6008c094f230434ca05134b135f3e9c3")

