# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaston(RPackage):
	"""Genetic Data Handling (QC, GRM, LD, PCA) & Linear Mixed Models

	Manipulation of genetic data (SNPs). Computation of GRM and dominance matrix, LD, heritability with efficient algorithms for linear mixed model (AIREML). Dandine et al <doi:10.1159/000488519>.
	"""
	
	cran = "gaston" 

	version("1.6", md5="862c863da43091a675b77de347cc1507")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
