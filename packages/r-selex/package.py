# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelex(RPackage):
	"""Functions for analyzing SELEX-seq data

	Tools for quantifying DNA binding specificities based on SELEX-seq data.
	"""
	
	homepage = "https://bussemakerlab.org/site/software/"
	bioc = "SELEX" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SELEX_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SELEX/SELEX_1.34.0.tar.gz"]

    version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="d2f6545f17a5e9c3ebee4cd1623b27a5ffa4425ba5f79607bb9dfba007808a54")

	depends_on("r-rjava@0.5.0:", type=("build", "run"))
	depends_on("r-biostrings@2.26:", type=("build", "run"))
	depends_on("openjdk@1.5:", type=("build", "link", "run"))
