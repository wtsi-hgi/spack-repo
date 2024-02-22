# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNblda(RPackage):
	"""Negative Binomial Linear Discriminant Analysis

	We proposed a package for the classification task which uses Negative Binomial distribution within Linear Discriminant Analysis (NBLDA). It is an extension of the 'PoiClaClu' package to Negative Binomial distribution. The classification algorithms are based on the papers Dong et al. (2016, ISSN: 1471-2105) and Witten, DM (2011, ISSN: 1932-6157) for NBLDA and PLDA, respectively. Although PLDA is a sparse algorithm and can be used for variable selection, the algorithm proposed by Dong et al. is not sparse. Therefore, it uses all variables in the classifier. Here, we extend Dong et al.'s algorithm to the sparse case by shrinking overdispersion towards 0 (Yu et al., 2013, ISSN: 1367-4803) and offset parameter towards 1 (as proposed by Witten DM, 2011). We support only the classification task with this version.
	"""
	
	cran = "NBLDA" 

	version("1.0.1", md5="43f9a8b2efc60c8abe96f710dc8eb308")

	depends_on("r-ggplot2", type=("build", "run"))
