# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsdfgs(RPackage):
	"""Training Set Determination for Genomic Selection

	We propose an optimality criterion to determine the required training set, r-score, which is derived directly from Pearson's correlation between the genomic estimated breeding values and phenotypic values of the test set <doi:10.1007/s00122-019-03387-0>. This package provides two main functions to determine a good training set and its size.
	"""
	
	homepage = "https://github.com/oumarkme/TSDFGS"
	cran = "TSDFGS" 

	version("2.0", md5="61d694401ef66ef6b30c39701bb06922")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
