# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlsylinks(RPackage):
	"""Utilities and Kinship Information for Research with the NLSY

	Utilities and kinship information for behavior genetics and
    developmental research using the National Longitudinal Survey of Youth
    (NLSY; <https://www.nlsinfo.org/>).
	"""
	
	homepage = "https://nlsy-links.github.io/NlsyLinks/"
	cran = "NlsyLinks" 

	version("2.2.1", md5="0756909d8121b0e760db29587983d29d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
