# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNomordr(RPackage):
	"""Randomization Test for Sequences of Nominal Values

	Implements the nomord_probe() function, which performs a statistical analysis on an input vector (sequence) of nominal (categorical) values.
	"""
	
	cran = "nomordR" 

	version("0.1", md5="f4b33150c7df9f55b8ee55f39a8f6974")

