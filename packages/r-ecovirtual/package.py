# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcovirtual(RPackage):
	"""Simulation of Ecological Models

	Computer simulations of classical ecological models as a
    learning resource.
	"""
	
	homepage = "http//ecovirtual.ib.usp.br"
	cran = "EcoVirtual" 

	version("1.1", md5="c16cb261319f28bd2d16f64059a8ae39")

