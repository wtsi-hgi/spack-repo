# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdaa(RPackage):
	"""Sampling: Design and Analysis

	Functions and Datasets from Lohr, S. (1999), Sampling:
        Design and Analysis, Duxbury.
	"""
	
	cran = "SDaA" 

	version("0.1-5", md5="d721019428d15a61d57a3d8b8f5f48b7")

