# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcc(RPackage):
	"""Parametric Bootstrapping to Control Rank Conditional Coverage

	Functions to implement the parametric and non-parametric bootstrap 
    confidence interval methods described in Morrison and Simon (2017) <arXiv:1702.06986>.
	"""
	
	homepage = "http://github.com/jean997/rcc"
	cran = "rcc" 

	version("1.0.0", md5="13d73e6311c59da7e303b7342c9f32a9")

