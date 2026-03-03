# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssertable(RPackage):
	"""Verbose Assertions for Tabular Data (Data.frames and
Data.tables)

	Simple, flexible, assertions on data.frame or data.table objects with verbose output for vetting. While other assertion packages apply towards more general use-cases, assertable is tailored towards tabular data. It includes functions to check variable names and values, whether the dataset contains all combinations of a given set of unique identifiers, and whether it is a certain length. In addition, assertable includes utility functions to check the existence of target files and to efficiently import multiple tabular data files into one data.table.
	"""
	
	cran = "assertable" 

	version("0.2.8", md5="f3a26aa7804750755d71d3b426b722c6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
