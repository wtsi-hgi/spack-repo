# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbmn(RPackage):
	"""Handling Linear Gaussian Bayesian Networks

	Creation, manipulation, simulation of linear Gaussian Bayesian
             networks from text files and more...
	"""
	
	cran = "rbmn" 

	version("0.9-6", md5="f03f8f2b08d28fee22200bfc19d424aa")

	depends_on("r-mass", type=("build", "run"))
