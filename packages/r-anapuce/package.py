# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnapuce(RPackage):
	"""Tools for Microarray Data Analysis

	Functions for normalisation, differentially analysis of microarray data and local False Discovery Rate.
	"""
	
	cran = "anapuce" 

	version("2.3", md5="24e53cda9610f36ffb63a0bda3ca66fb")

	depends_on("r@3.4:", type=("build", "run"))
