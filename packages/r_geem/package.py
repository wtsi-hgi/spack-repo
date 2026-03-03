# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeem(RPackage):
	"""Solve Generalized Estimating Equations

	GEE estimation of the parameters in mean structures with possible
    correlation between the outcomes. User-specified mean link and variance
    functions are allowed, along with observation weighting. The 'M' in the name
    'geeM' is meant to emphasize the use of the Matrix package, which allows for an
    implementation based fully in R.
	"""
	
	cran = "geeM" 

	version("0.10.1", md5="e493043dac3bd7c57b104ace2a6e19d7")

	depends_on("r-matrix", type=("build", "run"))
