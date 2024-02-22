# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKerseg(RPackage):
	"""New Kernel-Based Change-Point Detection

	New kernel-based test and fast tests for detecting change-points or changed-intervals where the distributions abruptly change. They work well particularly for high-dimensional data.
    Song, H. and Chen, H. (2022)
    <arXiv:2206.01853>.
	"""
	
	cran = "kerSeg" 

	version("1.1", md5="3374bb12178612639408412f793aab59")

	depends_on("r-rcpp", type=("build", "run"))
