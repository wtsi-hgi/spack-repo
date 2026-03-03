# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtbbeer(RPackage):
	"""US Beer Statistics from TTB

	U.S. Department of the Treasury, Alcohol and Tobacco Tax and
    Trade Bureau (TTB) collects data and reports on monthly beer
    industry production and operations. This data package includes
    a collection of 10 years (2006 - 2015) worth of data on materials
    used at U.S. breweries in pounds reported by the Brewer's Report
    of Operations and the Quarterly Brewer's Report of Operations
    forms, ready for data analysis. This package also includes historical
    tax rates on distilled spirits, wine, beer, champagne, and tobacco
    products as individual data sets.
	"""
	
	homepage = "https://github.com/jasdumas/ttbbeer"
	cran = "ttbbeer" 

	version("1.1.0", md5="dcd540adf008cb39f2bceef85b7a2372")

	depends_on("r@3.1.2:", type=("build", "run"))
