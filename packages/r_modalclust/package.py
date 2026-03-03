# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModalclust(RPackage):
	"""Hierarchical Modal Clustering

	Performs Modal Clustering (MAC) including Hierarchical Modal Clustering (HMAC) along with their parallel implementation (PHMAC) over several processors.  These model-based non-parametric clustering techniques can extract  clusters in very high dimensions with arbitrary density shapes. By default clustering is performed over several resolutions and the results are summarised as a hierarchical tree. Associated plot functions are also provided. There is a package vignette that provides many examples. This version adheres to CRAN policy of not spanning more than two child processes by default.
	"""
	
	cran = "Modalclust" 

	version("0.7", md5="595481b5f35c28b25b91e17a56a831cc")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
