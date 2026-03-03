# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCiperm(RPackage):
	"""Computationally-Efficient Confidence Intervals for Mean Shift
from Permutation Methods

	Implements computationally-efficient construction of
    confidence intervals from permutation or randomization tests
    for simple differences in means,
    based on Nguyen (2009) <doi:10.15760/etd.7798>.
	"""
	
	homepage = "https://github.com/ColbyStatSvyRsch/CIPerm/"
	cran = "CIPerm" 

	version("0.2.3", md5="eb8731ac16e6069028ea8fb828599075")

	depends_on("r-matrixstats", type=("build", "run"))
