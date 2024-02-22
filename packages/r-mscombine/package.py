# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMscombine(RPackage):
	"""Combine Data from Positive and Negative Ionization Mode Finding
Common Entities

	Find common entities detected in both positive and negative
    ionization mode, delete this entity in the less sensible mode and combine both
    matrices.
	"""
	
	cran = "MScombine" 

	version("1.4", md5="fb65dce2cf670e9902f2069799d700bc")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
