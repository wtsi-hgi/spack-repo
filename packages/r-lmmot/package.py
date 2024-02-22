# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmmot(RPackage):
	"""Multiple Ordinal Tobit (MOT) Model

	Fit right censored Multiple Ordinal Tobit (MOT) model.
	"""
	
	cran = "lmmot" 

	version("0.1.4", md5="477005faf46dddf853930bb25503cf89")

	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
