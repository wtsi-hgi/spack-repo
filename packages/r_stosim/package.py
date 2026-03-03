# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStosim(RPackage):
	"""Stochastic Simulator for Reliability Modeling of Repairable
Systems

	A toolkit for Reliability Availability and Maintainability (RAM) modeling of industrial process systems.
	"""
	
	cran = "stosim" 

	version("0.0.15", md5="f096b6232309ffab81a7b5f8d6037123")

	depends_on("r-rcpp", type=("build", "run"))
