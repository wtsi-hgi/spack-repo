# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyncrng(RPackage):
	"""A Synchronized Tausworthe RNG for R and Python

	Generate the same random numbers in R and Python.
	"""
	
	cran = "SyncRNG" 

	version("1.3.3", md5="06c3cc94328529b2d943a9df3d8ba9c0")

	depends_on("r@3:", type=("build", "run"))
