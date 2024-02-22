# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKsnn(RPackage):
	"""K* Nearest Neighbors Algorithm

	Prediction with k* nearest neighbor algorithm 
    based on a publication by Anava and Levy (2016) <arXiv:1701.07266>.
	"""
	
	cran = "ksNN" 

	version("0.1.2", md5="dda65020d0d86c46034bc7ae0f3017dc")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp@0.10.6:", type=("build", "run"))
