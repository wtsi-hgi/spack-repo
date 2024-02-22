# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCustosascensor(RPackage):
	"""Costs Allocation for the Installation of an Elevator

	Calculate the distribution of costs for the installation of an elevator based on the different distribution rules.
	"""
	
	cran = "CustosAscensor" 

	version("0.1.0", md5="5cbc6438164408877893a34ee92b702e")

