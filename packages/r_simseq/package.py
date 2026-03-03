# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimseq(RPackage):
	"""Nonparametric Simulation of RNA-Seq Data

	RNA sequencing analysis methods are often derived by relying on hypothetical parametric models for read counts that are not likely to be precisely satisfied in practice. Methods are often tested by analyzing data that have been simulated according to the assumed model. This testing strategy can result in an overly optimistic view of the performance of an RNA-seq analysis method. We develop a data-based simulation algorithm for RNA-seq data. The vector of read counts simulated for a given experimental unit has a joint distribution that closely matches the distribution of a source RNA-seq dataset provided by the user. Users control the proportion of genes simulated to be differentially expressed (DE) and can provide a vector of weights to control the distribution of effect sizes. The algorithm requires a matrix of RNA-seq read counts with large sample sizes in at least two treatment groups. Many datasets are available that fit this standard.
	"""
	
	cran = "SimSeq" 

	version("1.4.0", md5="bc0eac0087d31f3111ffd21f85eedbad")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
