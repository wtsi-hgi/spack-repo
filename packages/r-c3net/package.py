# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RC3net(RPackage):
	"""Inferring Large-Scale Gene Networks with C3NET

	Allows inferring gene regulatory networks
        with direct physical interactions from microarray expression
        data using C3NET.
	"""
	
	cran = "c3net" 

	version("1.1.1.1", md5="fc8a88bbff47e5a6124684c59b6e6f7a")

	depends_on("r@2.12.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
