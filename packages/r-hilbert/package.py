# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHilbert(RPackage):
	"""Coordinate Indexing on Hilbert Curves

	Provides utilities for encoding and decoding coordinates to/from Hilbert curves
  based on the iterative encoding implementation described in Chen et al. (2006) <doi:10.1002/spe.793>.
	"""
	
	homepage = "https://hilbert.justinsingh.me"
	cran = "hilbert" 

	version("0.2.1", md5="71fff7ec2e5e6853a73b0cb3d350dc29")

	depends_on("r-cpp11", type=("build", "run"))
