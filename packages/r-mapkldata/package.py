# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapkldata(RPackage):
	"""Gene expression data for testing of the package mAPKL.

	Gene expression data from a breast cancer study published by Turashvili et al. in 2007, provided as an eSet.
	"""
	
	bioc = "mAPKLData"

	version("1.34.0", commit="6620a67509196e84b79ecb1af246e24da2001454")

	depends_on("r@3.2:", type=("build", "run"))

