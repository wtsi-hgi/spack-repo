# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsl(RPackage):
	"""Latent Structure Learning

	Fits structural equation modeling via penalized likelihood.
	"""
	
	cran = "lsl" 

	version("0.5.6", md5="b07a9324452727239a9e5a66ba75d71e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
