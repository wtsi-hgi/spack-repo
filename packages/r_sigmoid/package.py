# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigmoid(RPackage):
	"""Sigmoid Functions for Machine Learning

	Several different sigmoid functions are implemented, including a wrapper function, SoftMax preprocessing and inverse functions.
	"""
	
	cran = "sigmoid" 

	version("1.4.0", md5="b97a0a98c6f7a37940025dee8e946b6a")

	depends_on("r@3.2.2:", type=("build", "run"))
