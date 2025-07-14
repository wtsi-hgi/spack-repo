# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSclcbam(RPackage):
	"""Sequence data from chromosome 4 of a small-cell lung tumor

	Whole-exome sequencing data from a murine small-cell lung tumor; only contains data of chromosome 4.
	"""
	
	bioc = "SCLCBam"

	version("1.40.0", commit="465c2abe16141879396fa235eb3851d26f85721e")
	version("1.34.0", commit="bd1780127d9bbc786f834e5c7715a0b8c0d7a429")

	depends_on("r@2.10:", type=("build", "run"))

