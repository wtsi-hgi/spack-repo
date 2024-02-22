# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRssop(RPackage):
	"""Simulation of Supply Reservoir Systems using Standard Operation
Policy

	Reservoir Systems Standard Operation Policy. A system for simulation of supply reservoirs. It proposes functionalities for plotting and evaluation of supply reservoirs systems.
	"""
	
	cran = "RSSOP" 

	version("1.1", md5="726f1b0963ea36fc9d7d6aac3cd68f90")

