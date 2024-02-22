# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpci(RPackage):
	"""Projection Pursuit for Cluster Identification

	Implements recently developed projection 
    pursuit algorithms for finding optimal linear cluster
    separators. The clustering algorithms use optimal
    hyperplane separators based on minimum density, Pavlidis et. al (2016) <http://jmlr.org/papers/volume17/15-307/15-307.pdf>;
    minimum normalised cut, Hofmeyr (2017) <doi:10.1109/TPAMI.2016.2609929>;
    and maximum variance ratio clusterability, Hofmeyr and Pavlidis (2015) <doi:10.1109/SSCI.2015.116>.
	"""
	
	cran = "PPCI" 

	version("0.1.5", md5="dd98b866a6571f5159221af6392d50ed")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
