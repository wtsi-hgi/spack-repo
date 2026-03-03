# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMstknnclust(RPackage):
	"""MST-kNN Clustering Algorithm

	Implements the MST-kNN clustering algorithm which was proposed by Inostroza-Ponta, M. (2008) <https://trove.nla.gov.au/work/28729389?selectedversion=NBD44634158>.  
	"""
	
	cran = "mstknnclust" 

	version("0.3.2", md5="ebcdb067cba4a14ce9407e43df115aba")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
