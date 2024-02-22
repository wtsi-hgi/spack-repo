# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoestrare(RPackage):
	"""Rare Variant Association Test Based on Position Density
Estimation

	Rare variant association test integrating variant position information. It aims to identify the presence of clusters of disease-risk variants in specific gene regions. For more details, please read the publication from Persyn et al. (2017)  <doi:10.1371/journal.pone.0179364>.
	"""
	
	cran = "DoEstRare" 

	version("0.2", md5="6208213f06402729a7b99d4d5605f4cf")

	depends_on("r@2.15:", type=("build", "run"))
