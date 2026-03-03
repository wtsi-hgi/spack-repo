# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimecol(RPackage):
	"""Simulation of Ecological (and Other) Dynamic Systems

	An object oriented framework to simulate
  ecological (and other) dynamic systems. It can be used for
  differential equations, individual-based (or agent-based) and other
  models as well. It supports structuring of simulation scenarios (to avoid copy
  and paste) and aims to improve readability and re-usability of code.
	"""
	
	homepage = "http://www.simecol.de/"
	cran = "simecol" 

	version("0.8-14", md5="b89a07dbe64805faca76e992be67c5ac")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
