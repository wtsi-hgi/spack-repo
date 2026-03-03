# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatman(RPackage):
	"""Convert Categorical Representations of Logicals to Actual
Logicals

	Survey systems and other third-party data sources commonly use non-standard representations of logical values when
    it comes to qualitative data - "Yes", "No" and "N/A", say. batman is a package designed to seamlessly convert these into logicals.
    It is highly localised, and contains equivalents to boolean values in languages including German, French, Spanish, Italian,
    Turkish, Chinese and Polish.
	"""
	
	homepage = "https://github.com/ironholds/batman"
	cran = "batman" 

	version("0.1.0", md5="f770a0bb8639d446d168534f6e73b4d0")

	depends_on("r-rcpp", type=("build", "run"))
