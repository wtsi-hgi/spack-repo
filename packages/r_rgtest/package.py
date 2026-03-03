# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgtest(RPackage):
	"""Robust Graph-Based Two-Sample Test

	Useful tools for determining whether two samples are from the same distribution. Utilizes a robust method to address the problematic structure of the similarity graph constructed from high-dimensional data. The method is provided in Yichuan Bai and Lynna Chu (2023) <arXiv:2307.12325>.
	"""
	
	cran = "rgTest" 

	version("0.1", md5="31f831767eacff9527623468fe1af30f")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
