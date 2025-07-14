# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrorna(RPackage):
	"""Data and functions for dealing with microRNAs

	Different data resources for microRNAs and some functions for manipulating them.
	"""
	
	bioc = "microRNA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/microRNA_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/microRNA/microRNA_1.60.0.tar.gz"]

    version("1.66.0", tag="RELEASE_3_21")
	version("1.60.0", sha256="fb8725d7247f4f08233138dcc38a683ae346afa3d5ef1a85dd276fe94b52c86a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biostrings@2.11.32:", type=("build", "run"))
