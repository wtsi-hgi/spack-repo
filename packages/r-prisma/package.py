# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrisma(RPackage):
	"""Protocol Inspection and State Machine Analysis

	Loads and processes huge text
    corpora processed with the sally toolbox (<http://www.mlsec.org/sally/>).
    sally acts as a very fast preprocessor which splits the text files into
    tokens or n-grams. These output files can then be read with the PRISMA
    package which applies testing-based token selection and has some
    replicate-aware, highly tuned non-negative matrix factorization and
    principal component analysis implementation which allows the processing of
    very big data sets even on desktop machines.
	"""
	
	cran = "PRISMA" 

	version("0.2-7", md5="97bda35dc208da926d4c02e1a1aab5aa")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
