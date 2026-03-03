# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssortnet(RPackage):
	"""Calculate the Assortativity Coefficient of Weighted and Binary
Networks

	Functions to calculate the assortment of vertices in social networks.  This can be measured on both weighted and binary networks, with discrete or continuous vertex values.
	"""
	
	cran = "assortnet" 

	version("0.20", md5="032fd8e7c6ce308e373c020ad838c5c5")

