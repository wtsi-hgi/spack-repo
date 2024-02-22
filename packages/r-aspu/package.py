# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAspu(RPackage):
	"""Adaptive Sum of Powered Score Test

	R codes for the (adaptive) Sum of Powered Score ('SPU' and 'aSPU')
    tests, inverse variance weighted Sum of Powered score ('SPUw' and 'aSPUw') tests
    and gene-based and some pathway based association tests (Pathway based Sum of
    Powered Score tests ('SPUpath'), adaptive 'SPUpath' ('aSPUpath') test, 'GEEaSPU'
    test for multiple traits - single 'SNP' (single nucleotide polymorphism)
    association in generalized estimation equations, 'MTaSPUs' test for multiple
    traits - single 'SNP' association with Genome Wide Association Studies ('GWAS')
    summary statistics, Gene-based Association Test that uses an extended 'Simes'
    procedure ('GATES'), Hybrid Set-based Test ('HYST') and extended version
    of 'GATES' test for pathway-based association testing ('GATES-Simes'). ).
    The tests can be used with genetic and other data sets with covariates. The
    response variable is binary or quantitative. Summary; (1) Single trait-'SNP' set
    association with individual-level data ('aSPU', 'aSPUw', 'aSPUr'), (2) Single trait-'SNP'
    set association with summary statistics ('aSPUs'), (3) Single trait-pathway
    association with individual-level data ('aSPUpath'), (4) Single trait-pathway
    association with summary statistics ('aSPUsPath'), (5) Multiple traits-single
    'SNP' association with individual-level data ('GEEaSPU'), (6) Multiple traits-
    single 'SNP' association with summary statistics ('MTaSPUs'), (7) Multiple traits-'SNP' set association with summary statistics('MTaSPUsSet'), (8) Multiple traits-pathway association with summary statistics('MTaSPUsSetPath').
	"""
	
	homepage = "https://github.com/ikwak2/aSPU"
	cran = "aSPU" 

	version("1.50", md5="e39666be4d206fd0a9f0d68bbe64e9f8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-gee", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
