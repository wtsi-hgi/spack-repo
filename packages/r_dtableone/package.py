# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtableone(RPackage):
	"""Tabular Comparison of Paired Diagnostic Tests

	Offers statistical methods to compare diagnostic performance between two binary diagnostic tests on the same subject in clinical studies. Includes functions for generating formatted tables to display diagnostic outcomes, facilitating a clear and comprehensive comparison directly through the R console. Inspired by and extending the functionalities of the 'DTComPair', 'tableone', and 'gtsummary' packages.
	"""
	
	cran = "Dtableone" 

	version("1.1.0", md5="c238de83b81222eafa0e15cffb642e39")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-epir@2.0.61:", type=("build", "run"))
	depends_on("r-irr@0.84.1:", type=("build", "run"))
	depends_on("r-proc@1.18.5:", type=("build", "run"))
