# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixdist(RPackage):
	"""Finite Mixture Distribution Models

	Fit finite mixture distribution models to grouped data and conditional data by maximum likelihood using a combination of a Newton-type algorithm and the EM algorithm.
	"""
	
	homepage = "https://www.r-project.org/"
	cran = "mixdist" 

	version("0.5-5", md5="0903e021702ee9ed0d5eb8bec58a26f1")

	depends_on("r@1.4:", type=("build", "run"))
