# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBar(RPackage):
	"""Bayesian Adaptive Randomization

	Bayesian adaptive randomization is also called outcome adaptive randomization, which is increasingly used in clinical trials.
	"""
	
	cran = "BAR" 

	version("0.1.1", md5="a8e7325fb150ae64fca1a5590350f7a4")

