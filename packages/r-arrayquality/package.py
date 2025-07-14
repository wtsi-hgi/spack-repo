# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrayquality(RPackage):
	"""Assessing array quality on spotted arrays

	Functions for performing print-run and array level quality assessment.
	"""
	
	homepage = "http://arrays.ucsf.edu/"
	bioc = "arrayQuality"

	version("1.86.0", commit="d6ef47d7c3f6fe2d54ceaa9b5e32d4477a78aab6")
	version("1.80.0", commit="0c752d234118005baf28fbd062eb8aea83bf09c5")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
