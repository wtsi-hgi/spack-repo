# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenfordAnalysis(RPackage):
	"""Benford Analysis for Data Validation and Forensic Analytics

	Provides tools that make it easier to validate data using Benford's Law.
	"""
	
	homepage = "http://github.com/carloscinelli/benford.analysis"
	cran = "benford.analysis" 

	version("0.1.5", md5="9e2e2f2182c40d45109cc1ddb4257bce")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
