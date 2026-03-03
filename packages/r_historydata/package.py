# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHistorydata(RPackage):
	"""Data Sets for Historians

	These sample data sets are intended for historians
    learning R. They include population, institutional, religious,
    military, and prosopographical data suitable for mapping,
    quantitative analysis, and network analysis.
	"""
	
	homepage = "https://github.com/ropensci/historydata"
	cran = "historydata" 

	version("0.1", md5="ae954aedb1ba749b209abbab04690b33")

	depends_on("r@3.0.2:", type=("build", "run"))
