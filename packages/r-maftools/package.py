# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaftools(RPackage):
	"""Summarize, Analyze and Visualize MAF Files

	Analyze and visualize Mutation Annotation Format (MAF) files from large scale sequencing studies. This package provides various functions to perform most commonly used analyses in cancer genomics and to create feature rich customizable visualzations with minimal effort.
	"""
	
	homepage = "https://github.com/PoisonAlien/maftools"
	bioc = "maftools"

	version("2.24.0", commit="e3a5f178a41bb04e7cbece5660541a41ac89c1aa")
	version("2.18.0", commit="b1f86254fd4309c7434087ad497a26e763b4cc4d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rhtslib", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
