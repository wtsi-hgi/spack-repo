# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpinet(RPackage):
	"""Epidemic/Network-Related Tools

	A collection of epidemic/network-related tools. Simulates transmission of diseases through contact networks. Performs Bayesian inference on network and epidemic parameters, given epidemic data.
	"""
	
	cran = "epinet" 

	version("2.1.11", md5="43e25b5027f7580670dce19d42e9dc8e")

	depends_on("r-network", type=("build", "run"))
