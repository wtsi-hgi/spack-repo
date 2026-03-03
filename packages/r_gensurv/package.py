# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGensurv(RPackage):
	"""Generating Multi-State Survival Data

	Generation of survival data with one (binary)
  time-dependent covariate.  Generation of survival data arising
  from a progressive illness-death model.
	"""
	
	homepage = "https://github.com/arturstat/genSurv"
	cran = "genSurv" 

	version("1.0.4", md5="7a80dd868d03828aa82b1f992bca1557")

	depends_on("r@2.12:", type=("build", "run"))
