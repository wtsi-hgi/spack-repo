# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmf(RPackage):
	"""Functions for Estimation and Inference of Selection in
Age-Structured Populations

	Provides methods for estimation and statistical
               inference on directional and fluctuating selection in age-structured
               populations.
	"""
	
	cran = "lmf" 

	version("1.2.1", md5="f950433b9e6597f29cba039fa004a9ab")

