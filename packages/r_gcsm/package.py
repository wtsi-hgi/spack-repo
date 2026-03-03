# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcsm(RPackage):
	"""Implements Generic Composite Similarity Measure

	Provides implementation of the generic composite similarity measure
    (GCSM) described in Liu et al. (2020) <doi:10.1016/j.ecoinf.2020.101169>. The
    implementation is in C++ and uses 'RcppArmadillo'. Additionally, implementations
    of the structural similarity (SSIM) and the composite similarity measure based
    on means, standard deviations, and correlation coefficient (CMSC), are included.
	"""
	
	homepage = "https://github.com/liuyadong/GCSM"
	cran = "GCSM" 

	version("0.1.1", md5="689c3f706796b3dbc36549893a2005c3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
