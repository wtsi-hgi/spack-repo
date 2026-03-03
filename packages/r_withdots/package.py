# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWithdots(RPackage):
	"""Put ... in a Function's Argument List

	Adds ... to a function's argument list so that it can
    tolerate non-matching arguments.
	"""
	
	homepage = "https://github.com/NikKrieger/withdots"
	cran = "withdots" 

	version("0.1.1", md5="8daa2fb8df0c51d6ca17dace43037b75")

