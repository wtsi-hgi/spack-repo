# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdmod(RPackage):
	"""Proximal/Distal Modeling Framework for Pavlovian Conditioning
Phenomena

	Fits a model of Pavlovian conditioning phenomena, such as response extinction and spontaneous recovery, and partial reinforcement extinction effects. Competing proximal and distal reward predictions, computed using fast and slow learning rates, combine according to their uncertainties and the recency of information. The resulting mean prediction drives the response rate.
	"""
	
	cran = "pdmod" 

	version("1.0.1", md5="bd2419d063eb8bb6add069b0c91af224")

	depends_on("r-mco", type=("build", "run"))
