# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAc3net(RPackage):
	"""Inferring Directional Conservative Causal Core Gene Networks

	Infers directional conservative causal core (gene) networks. It is an advanced version of the algorithm C3NET by providing directional network. Gokmen Altay (2018) <doi:10.1101/271031>, bioRxiv.
	"""
	
	cran = "Ac3net" 

	version("1.2.2", md5="3bb784a260f3754e7c265660684ffbe0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
