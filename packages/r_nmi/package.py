# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmi(RPackage):
	"""Normalized Mutual Information of Community Structure in Network

	Calculates the normalized mutual information (NMI) of two community structures in network analysis.
	"""
	
	cran = "NMI" 

	version("2.0", md5="4c7ff8b6dc4834b2cfbe0b8cc9b5d88a")

	depends_on("r@3.2.2:", type=("build", "run"))
