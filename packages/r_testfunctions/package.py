# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestfunctions(RPackage):
	"""Test Functions for Simulation Experiments and Evaluating
Optimization and Emulation Algorithms

	Test functions are often used to test computer code.
  They are used in optimization to test algorithms and in
  metamodeling to evaluate model predictions. This package provides
  test functions that can be used for any purpose.
	"""
	
	cran = "TestFunctions" 

	version("0.2.1", md5="273fbd96aa6d68cf4f151804520bbf87")

