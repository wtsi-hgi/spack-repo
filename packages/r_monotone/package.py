# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonotone(RPackage):
	"""Performs Monotone Regression

	The monotone package contains a fast up-and-down-blocks implementation for the pool-adjacent-violators algorithm 
  for simple linear ordered monotone regression, including two spin-off functions
  for unimodal and bivariate monotone regression (see <doi:10.18637/jss.v102.c01>).
	"""
	
	cran = "monotone" 

	version("0.1.2", md5="5b9ed2a51df81b107bde640c36957814")

