# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMar1s(RPackage):
	"""Multiplicative AR(1) with Seasonal Processes

	Multiplicative AR(1) with Seasonal is a stochastic
  process model built on top of AR(1). The package provides the
  following procedures for MAR(1)S processes: fit, compose, decompose,
  advanced simulate and predict.
	"""
	
	homepage = "https://github.com/aparamon/mar1s"
	cran = "mar1s" 

	version("2.1.1", md5="03c3c3791c0b9d3cbeda368533206b55")

	depends_on("r-cmrutils", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
