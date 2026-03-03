# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethodcompare(RPackage):
	"""Bias and Precision Plots

	Implementation of the methodology from the paper entitled
    "Effective plots to assess bias and precision in method comparison studies"
    published in Statistical Methods in Medical Research, P. Taffé (2018) <doi:10.1177/0962280218759693>.
	"""
	
	cran = "MethodCompare" 

	version("0.1.2", md5="23facf3fcae5a4454a4e3544a12c15ef")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
