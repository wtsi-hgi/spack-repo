# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsfar(RPackage):
	"""Seasonal Functional Autoregressive Models

	This is a collection of functions designed for simulating, estimating and forecasting seasonal functional autoregressive time series of order one. These methods are addressed in the manuscript: <https://www.monash.edu/business/ebs/research/publications/ebs/wp16-2019.pdf>.
	"""
	
	homepage = "https://github.com/haghbinh/Rsfar"
	cran = "Rsfar" 

	version("0.0.1", md5="8665f3c887b63a859a6ed0b2354e9aa1")

	depends_on("r-fda", type=("build", "run"))
