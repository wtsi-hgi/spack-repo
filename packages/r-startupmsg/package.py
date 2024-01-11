# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RStartupmsg(RPackage):
	"""Utilities for Start-Up Messages

	Provides utilities to create or suppress start-up messages.
	"""
	
	cran = "startupmsg" 

	version("0.9.6", md5="d9bb261e2964199f537f447af8672c91")

	depends_on("r@1.8.0:", type=("build", "run"))

