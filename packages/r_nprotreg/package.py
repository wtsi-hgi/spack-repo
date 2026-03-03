# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNprotreg(RPackage):
	"""Nonparametric Rotations for Sphere-Sphere Regression

	Fits sphere-sphere regression models by estimating locally weighted
    rotations. Simulation of sphere-sphere data according to non-rigid rotation
    models. Provides methods for bias reduction applying iterative procedures
    within a Newton-Raphson learning scheme. Cross-validation is exploited to select
    smoothing parameters. See Marco Di Marzio, Agnese Panzera & Charles C. Taylor
    (2018) <doi:10.1080/01621459.2017.1421542>.
	"""
	
	cran = "nprotreg" 

	version("1.1.1", md5="d6aaaf69c61aeb2ea74357fdb18812c2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
