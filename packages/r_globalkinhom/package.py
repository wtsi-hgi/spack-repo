# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlobalkinhom(RPackage):
	"""Inhomogeneous K- And Pair Correlation Functions Using Global
Estimators

	Second-order summary statistics K- and pair-correlation functions describe
    interactions in point pattern data. This package provides computations to estimate those
    statistics on inhomogeneous point processes, using the methods of
    in T Shaw, J Møller, R Waagepetersen, 2020 <arXiv:2004.00527>.
	"""
	
	cran = "globalKinhom" 

	version("0.1.7", md5="154bfb3cc10a50399a13beba455d91d5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat-random@2.1:", type=("build", "run"))
	depends_on("r-spatstat-explore@3:", type=("build", "run"))
	depends_on("r-spatstat-geom@3.1:", type=("build", "run"))
