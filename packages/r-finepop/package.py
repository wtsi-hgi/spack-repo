# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinepop(RPackage):
	"""Fine-Scale Population Analysis

	Statistical tool set for population genetics. The package provides following functions: 1) empirical Bayes estimator of Fst and other measures of genetic differentiation, 2) regression analysis of environmental effects on genetic differentiation using bootstrap method, 3) interfaces to read and manipulate 'GENEPOP' format data files and allele/haplotype frequency format files.
	"""
	
	cran = "FinePop" 

	version("1.5.2", md5="c484b2f6b24bc3fd75380446090d3739")
	version("1.5.1", md5="073699df24fd4854c22c7eef88727f1d")

	depends_on("r@4:", type=("build", "run"))
