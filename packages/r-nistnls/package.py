# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNistnls(RPackage):
	"""Nonlinear least squares examples from NIST

	Datasets for testing nonlinear regression routines.
	"""
	
	cran = "NISTnls" 

	version("0.9-13", md5="f519a96f115b5793cd0bb9533d88c5b5")

	depends_on("r@2.14:", type=("build", "run"))
