# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReset(RPackage):
	"""Reconstruction Set Test

	Contains logic for sample-level variable set scoring using randomized reduced rank reconstruction error. 
  Frost, H. Robert (2023) "Reconstruction Set Test (RESET): a computationally efficient method for 
  single sample gene set testing based on randomized reduced rank reconstruction error" <doi:10.1101/2023.04.03.535366>.
	"""
	
	cran = "RESET" 

	version("0.2.1", md5="2ac01fb78871c57a47497c03dc46f76a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
