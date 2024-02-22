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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/maftools_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/maftools/maftools_2.18.0.tar.gz"]

	version("2.18.0", md5="3dadc2b7f6f1693ae23a41b61f541db4")

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
