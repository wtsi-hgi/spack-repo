# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSasmixed(RPackage):
	"""Data sets from "SAS System for Mixed Models"

	Data sets and sample lmer analyses corresponding
  to the examples in Littell, Milliken, Stroup and Wolfinger
  (1996), "SAS System for Mixed Models", SAS Institute.
	"""
	
	cran = "SASmixed" 

	version("1.0-4", md5="7d4727e2c81d70a8a18046ab07ed34e3")

	depends_on("r@2.14:", type=("build", "run"))
