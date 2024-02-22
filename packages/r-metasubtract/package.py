# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetasubtract(RPackage):
	"""Subtracting Summary Statistics of One or more Cohorts from
Meta-GWAS Results

	If results from a meta-GWAS are used for validation in one of the cohorts that was included in the meta-analysis, this will yield biased (i.e. too optimistic) results. 
      The validation cohort needs to be independent from the meta-Genome-Wide-Association-Study (meta-GWAS) results. 
      'MetaSubtract' will subtract the results of the respective cohort from the meta-GWAS results analytically without having to redo the meta-GWAS analysis using the leave-one-out methodology. 
      It can handle different meta-analyses methods and takes into account if single or double genomic control correction was applied to the original meta-analysis. 
      It can also handle different meta-analysis methods. It can be used for whole GWAS, but also for a limited set of genetic markers. 
      See for application: Nolte I.M. et al. (2017); <doi: 10.1038/ejhg.2017.50>.
	"""
	
	cran = "MetaSubtract" 

	version("1.60", md5="7ece6381271387e3213f6a5062e9ca7b")

