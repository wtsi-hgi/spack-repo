# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfexpand(RPackage):
	"""Automatically Expand Delimited Column Values into Multiple
Binary Columns with 'dfexpand'

	Implements an algorithm to effortlessly split a column in an R data frame filled with multiple values separated by delimiters. This automates the process of creating separate columns for each unique value, transforming them into binary outcomes.
	"""
	
	homepage = "https://github.com/jlpainter/dfexpand"
	cran = "dfexpand" 

	version("0.0.2", md5="d8f2eb85ae5e8e1dd01a57d3bc98be70")

	depends_on("r-stringr", type=("build", "run"))
