# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFipio(RPackage):
	"""Lightweight Federal Information Processing System (FIPS) Code
Information Retrieval

	Provides a lightweight suite
             of functions for retrieving information
             about 5-digit or 2-digit US FIPS codes.
	"""
	
	homepage = "https://fipio.justinsingh.me"
	cran = "fipio" 

	version("1.1.2", md5="2e540166bafa13efd74bc2982d304434")

	depends_on("r@3.5:", type=("build", "run"))
