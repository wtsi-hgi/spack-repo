# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpest(RPackage):
	"""Estimating Finite Population Total

	Given the values of sampled units and selection probabilities 
             the desraj function  in the package computes the estimated value of the total
             as well as estimated variance.
	"""
	
	cran = "fpest" 

	version("0.1.1", md5="3948470c0ffa61a7a965945b8e3e6559")

