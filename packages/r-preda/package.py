# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreda(RPackage):
	"""Position Related Data Analysis

	Package for the position related analysis of quantitative functional genomics data.
	"""
	
	bioc = "PREDA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PREDA_1.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PREDA/PREDA_1.48.0.tar.gz"]

	version("1.48.0", md5="6f051dc3182b2d70715d84a12e39dd57")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-lokern@1.0.9:", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
