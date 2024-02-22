# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrowth(RPackage):
	"""Multivariate Normal and Elliptically-Contoured Repeated
Measurements Models

	Functions for fitting various normal theory (growth
    curve) and elliptically-contoured repeated measurements models
    with ARMA and random effects dependence.
	"""
	
	homepage = "http://www.commanster.eu/rcode.html"
	cran = "growth" 

	version("1.1.1", md5="677053c2cc5bdca2ab88d7804506a8d8")

	depends_on("r@1.4:", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
