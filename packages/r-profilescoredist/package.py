# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfilescoredist(RPackage):
	"""Profile score distributions

	Regularization and score distributions for position count matrices.
	"""
	
	bioc = "profileScoreDist" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/profileScoreDist_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/profileScoreDist/profileScoreDist_1.30.0.tar.gz"]

	version("1.30.0", md5="59d0f0bd369e20aa7be8352e5cf46830")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
