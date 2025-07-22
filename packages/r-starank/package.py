# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarank(RPackage):
	"""Stability Ranking

	Detecting all relevant variables from a data set is challenging, especially when only few samples are available and data is noisy. Stability ranking provides improved variable rankings of increased robustness using resampling or subsampling.
	"""
	
	bioc = "staRank" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/staRank_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/staRank/staRank_1.44.0.tar.gz"]

	version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="149d38d9e5128b4c53159ac517c81cff3a55eda5cb293dad12e159121b6515d9")

	depends_on("r-cellhts2", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
