# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtwrappers(RPackage):
	"""Simplified Data Analysis with Wrapper Functions for the
'Data.Table' Package

	Provides functionality for users who are learning R or the techniques of data analysis.  Written as a collection of wrapper functions, the 'DTwrapper' package facilitates many core operations of data processing.  This is achieved with relatively few requirements about the order of the processing steps or knowledge of specialized syntax.  'DTwrappers' creates coding results along with translations to data.table's code.  This enables users to benefit from the speed and efficiency of data.table's calculations.  Furthermore, the package also provides the translated code for educational purposes so that users can review working examples of coding syntax and calculations.
	"""
	
	cran = "DTwrappers" 

	version("0.0.2", md5="ff91b02ef7a0e6f9bbfcfdc0ea19100a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
