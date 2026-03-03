# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtauchen(RPackage):
	"""Discretization of AR(1) Processes

	Discretize AR(1) process following Tauchen (1986) <http://www.sciencedirect.com/science/article/pii/0165176586901680>. A discrete Markov chain that approximates in the sense of weak convergence a continuous-valued univariate Autoregressive process of first order is generated. It is a popular method used in economics and in finance. 
	"""
	
	homepage = "https://github.com/davidzarruk/Rtauchen"
	cran = "Rtauchen" 

	version("1.0", md5="16130074626b19fc72184faa3a8550f8")

