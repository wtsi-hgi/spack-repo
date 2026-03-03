# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIaliquor(RPackage):
	"""Monthly Iowa Liquor Sales Summary

	Provides a monthly summary of Iowa liquor (class E) sales from January 2015
    to October 2020. See the package website for more information, 
    documentation and examples. Data source: 
    Iowa Data portal <https://data.iowa.gov/resource/m3tr-qhgy.csv>.
	"""
	
	cran = "ialiquor" 

	version("0.1.0", md5="771765d660f81025c1d3c18da7d2ce74")

	depends_on("r@2.10:", type=("build", "run"))
