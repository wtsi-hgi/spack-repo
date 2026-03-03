# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbeta2009(RPackage):
	"""The Beta Random Number and Dirichlet Random Vector Generating
Functions

	The package contains functions to generate random numbers
        from the beta distribution and random vectors from the
        Dirichlet distribution.
	"""
	
	cran = "rBeta2009" 

	version("1.0", md5="38000662ab8b2318b24447ca0bfa984b", url="https://cran.r-project.org/src/contrib/rBeta2009_1.0.tar.gz")

