# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoubleexpseq(RPackage):
	"""Differential Exon Usage Test for RNA-Seq Data via Empirical
Bayes Shrinkage of the Dispersion Parameter

	Differential exon usage test for RNA-Seq data via an empirical Bayes shrinkage method for the dispersion parameter the utilizes inclusion-exclusion data to analyze the propensity to skip an exon across groups. The input data consists of two matrices where each row represents an exon and the columns represent the biological samples. The first matrix is the count of the number of reads expressing the exon for each sample. The second matrix is the count of the number of reads that either express the exon or explicitly skip the exon across the samples, a.k.a. the total count matrix. Dividing the two matrices yields proportions representing the propensity to express the exon versus skipping the exon for each sample.
	"""
	
	cran = "DoubleExpSeq" 

	version("1.1", md5="dadeeaf9002c6150095e856591f72d1e")

	depends_on("r-numderiv", type=("build", "run"))
