# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirai(RPackage):
	"""Minimalist Async Evaluation Framework for R

	Lightweight parallel code execution and distributed computing.
    Designed for simplicity, a 'mirai' evaluates an R expression asynchronously,
    on local or network resources, resolving automatically upon completion.
    Efficient scheduling over fast inter-process communications or secure TLS
    connections over TCP/IP, built on 'nanonext' and 'NNG' (Nanomsg Next Gen).
	"""
	
	homepage = "https://shikokuchuo.net/mirai/"
	cran = "mirai" 

	version("0.12.1", md5="4cb681ad70cae33c8e2a77eb33e5fbd1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nanonext@0.12:", type=("build", "run"))
