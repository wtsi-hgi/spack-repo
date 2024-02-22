# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneticsubsetter(RPackage):
	"""Identify Favorable Subsets of Germplasm Collections

	Finds subsets of sets of genotypes with a high Heterozygosity, and Mean of Transformed Kinships (MTK), measures that can indicate a subset would be beneficial for rare-trait discovery and genome-wide association scanning, respectively.
	"""
	
	cran = "GeneticSubsetter" 

	version("0.8", md5="844f7e0587a70c4ae11ea3e4b4a6bc1b")

