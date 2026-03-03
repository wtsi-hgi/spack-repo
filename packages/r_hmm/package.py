# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmm(RPackage):
	"""Hidden Markov Models

	Easy to use library to setup, apply and make inference with discrete time and discrete space Hidden Markov Models.
	"""
	
	homepage = "www.linhi.de"
	cran = "HMM" 

	version("1.0.1", md5="459504427d256777a528dbb04db0c7d4")

	depends_on("r@2:", type=("build", "run"))
