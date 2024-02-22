# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlr(RPackage):
	"""Bayesian Linear Regression

	Bayesian Linear Regression.
	"""
	
	cran = "BLR" 

	version("1.6", md5="e12b9c6b3d93eb9dc9d8c191cc71dc65")

	depends_on("r@3.1.2:", type=("build", "run"))
