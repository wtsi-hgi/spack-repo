# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovcombr(RPackage):
	"""Combine Partial Covariance / Relationship Matrices

	Combine partial covariance matrices using a Wishart-EM algorithm. 
    Methods are described in the November 2019 article by Akdemir et al. 
    <https://www.biorxiv.org/content/10.1101/857425v1>.
    It can be used to combine partially overlapping covariance matrices 
    from independent trials, partially overlapping multi-view relationship
    data from genomic experiments, partially overlapping Gaussian graphs
    described by their covariance structures. 
    High dimensional covariance estimation, 
    multi-view data integration.
    high dimensional covariance graph estimation.
	"""
	
	cran = "CovCombR" 

	version("1.0", md5="785f87020f13f3c02d8df107464032c0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-cholwishart", type=("build", "run"))
