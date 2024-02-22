# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlogis(RPackage):
	"""Fitting and Testing Generalized Logistic Distributions

	Tools for the generalized logistic distribution (Type I,
             also known as skew-logistic distribution), encompassing
	     basic distribution functions (p, q, d, r, score), maximum
	     likelihood estimation, and structural change methods.
	"""
	
	cran = "glogis" 

	version("1.0-2", md5="a139b20ec4ec8c9066bc2337dd728ef9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
