# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZiprop(RPackage):
	"""Permutations Tests and Performance Indicator for Zero-Inflated
Proportions Response

	Permutations tests to identify factor correlated to zero-inflated proportions response. Provide a performance indicator based on Spearman correlation to quantify the part of correlation explained by the selected set of factors. See details for the method at the following preprint e.g.: <https://hal.archives-ouvertes.fr/hal-02936779v3>. 
	"""
	
	homepage = "https://gitlab.paca.inrae.fr/meribaud/ziprop"
	cran = "ZIprop" 

	version("0.1.1", md5="aad4f978f34107fd4d8e412a4c6726ba")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
