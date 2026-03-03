# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeodadata(RPackage):
	"""Spatial Analysis Datasets for Teaching

	Stores small spatial datasets used to teach basic spatial analysis
    concepts. Datasets are based off of the 'GeoDa' software workbook and data
    site <https://geodacenter.github.io/data-and-lab/> developed by Luc Anselin
    and team at the University of Chicago. Datasets are stored as 'sf' objects.
	"""
	
	homepage = "https://github.com/spatialanalysis/geodaData"
	cran = "geodaData" 

	version("0.1.0", md5="6623fdce4008fb527438f8f836adc41e")

	depends_on("r@3.3:", type=("build", "run"))
