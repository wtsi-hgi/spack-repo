# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupc(RPackage):
	"""The Self-Updating Process Clustering Algorithms

	Implements the self-updating process clustering algorithms proposed
    in Shiu and Chen (2016) <doi:10.1080/00949655.2015.1049605>.
	"""
	
	homepage = "https://github.com/wush978/supc"
	cran = "supc" 

	version("0.2.6.2", md5="5338d59a93e0de5ea3c74658de3454d8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-bh@1.62:", type=("build", "run"))
