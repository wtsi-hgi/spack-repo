# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFusionclust(RPackage):
	"""Clustering and Feature Screening using L1 Fusion Penalty

	Provides the Big Merge Tracker and COSCI algorithms for convex clustering and 
    feature screening using L1 fusion penalty. See Radchenko, P. and Mukherjee, G. (2017) <doi:10.1111/rssb.12226> and 
    T.Banerjee et al. (2017) <doi:10.1016/j.jmva.2017.08.001> for more details.
	"""
	
	homepage = "https://github.com/trambakbanerjee/fusionclust"
	cran = "fusionclust" 

	version("1.0.0", md5="f0846513c0baab36a7fc450248ec557b")

	depends_on("r@3.4.1:", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
