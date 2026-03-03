# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoiltaxonomy(RPackage):
	"""A System of Soil Classification for Making and Interpreting Soil
Surveys

	Taxonomic dictionaries, formative element lists, and functions related to the maintenance, development and application of U.S. Soil Taxonomy. 
   Data and functionality are based on official U.S. Department of Agriculture sources including the latest edition of the Keys to Soil Taxonomy. Descriptions and metadata are obtained from the National Soil Information System or Soil Survey Geographic databases. Other sources are referenced in the data documentation. 
   Provides tools for understanding and interacting with concepts in the U.S. Soil Taxonomic System. Most of the current utilities are for working with taxonomic concepts at the "higher" taxonomic levels: Order, Suborder, Great Group, and Subgroup.
	"""
	
	homepage = "https://github.com/ncss-tech/SoilTaxonomy"
	cran = "SoilTaxonomy" 

	version("0.2.4", md5="2d100333e53541eaec98b157b126edf0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
