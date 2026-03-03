# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrtcomboFactorialexpSr(RPackage):
	"""Generation of Treatment Combination (in Standard Order) in 2^n
Factorial Experiment

	Gives the required 2^n treatment combinations in a 2^n symmetric factorial experiment in their respective standard order.
	"""
	
	cran = "TrtCombo.FactorialExp.SR" 

	version("4.0.4", md5="2b27a449acfee9f888d9f66a86380bf4")

