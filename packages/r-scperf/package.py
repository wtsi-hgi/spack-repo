# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScperf(RPackage):
	"""Functions for Planning and Managing Inventories in a Supply
Chain

	Implements different inventory models, the bullwhip effect and other supply chain performance variables. Marchena Marlene (2010) <arXiv:1009.3977>.
	"""
	
	cran = "SCperf" 

	version("1.1.1", md5="09a48b88d0cf832265d29bb1fd72e92c")

