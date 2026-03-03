# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlsmicrobio(RPackage):
	"""Nonlinear Regression in Predictive Microbiology

	Data sets and nonlinear regression models dedicated to predictive microbiology.
	"""
	
	homepage = "https://github.com/lbbe-software/nlsMicrobio"
	cran = "nlsMicrobio" 

	version("1.0-0", md5="40b2e56928e13305c1c7856afb963e13")

	depends_on("r-nlstools", type=("build", "run"))
