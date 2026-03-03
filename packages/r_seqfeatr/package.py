# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqfeatr(RPackage):
	"""A Tool to Associate FASTA Sequences and Features

	Provides user friendly methods for the identification of sequence patterns that are statistically significantly associated with a property of the sequence. For instance, SeqFeatR allows to identify viral immune escape mutations for hosts of given HLA types. The underlying statistical method is Fisher's exact test, with appropriate corrections for multiple testing, or Bayes. Patterns may be point mutations or n-tuple of mutations. SeqFeatR offers several ways to visualize the results of the statistical analyses, see Budeus (2016) <doi:10.1371/journal.pone.0146409>.
	"""
	
	cran = "SeqFeatR" 

	version("0.3.1", md5="4695b599ef71176addbea135c8c1245c")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-widgettools", type=("build", "run"))
	depends_on("r-calibrate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
