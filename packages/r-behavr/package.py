# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBehavr(RPackage):
	"""Canonical Data Structure for Behavioural Data

	Implements an S3 class based on 'data.table' to store and process efficiently ethomics (high-throughput behavioural) data.
	"""
	
	homepage = "https://github.com/rethomics/behavr"
	cran = "behavr" 

	version("0.3.2", md5="6f9ba82f4e9901369e27e78850ef1f04")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
