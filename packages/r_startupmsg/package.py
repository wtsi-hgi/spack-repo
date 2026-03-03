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

	version("0.9.6.1", md5="a3323b47b5dd36fd9db3197c400a1d84")

	depends_on("r@1.8:", type=("build", "run"))
