# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSerieslcb(RPackage):
	"""Lower Confidence Bounds for Binomial Series System

	Calculate and compare lower confidence bounds for binomial series system reliability. The R 'shiny' application, launched by the function launch_app(), weaves together a workflow of customized simulations and delta coverage calculations to output recommended lower confidence bound methods.
	"""
	
	cran = "serieslcb" 

	version("0.4.0", md5="7a640bb756bf13e2d7ae2f1a2fffb2ab")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
