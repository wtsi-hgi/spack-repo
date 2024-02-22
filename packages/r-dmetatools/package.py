# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmetatools(RPackage):
	"""Computational Tools for Meta-Analysis of Diagnostic Accuracy
Test

	Computational tools for meta-analysis of diagnostic accuracy test. Bootstrap-based computational methods of the confidence interval for AUC of summary ROC curve and some related AUC-based inference methods are available (Noma et al. (2021) <doi:10.1080/23737484.2021.1894408>).
	"""
	
	cran = "dmetatools" 

	version("1.1.1", md5="faf033f8b6ad736f97ca9f5345978574")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mada", type=("build", "run"))
