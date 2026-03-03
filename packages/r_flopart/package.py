# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlopart(RPackage):
	"""Functional Labeled Optimal Partitioning

	
 Provides an efficient 'C++' code for computing an
 optimal segmentation model
 with Poisson loss,
 up-down constraints,
 and label constraints,
 as described by Kaufman et al. (2022) <arXiv:2210.02580>.
	"""
	
	cran = "FLOPART" 

	version("2023.8.31", md5="9b0639630f17e5dc6c1f8eb02fb9d77e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
