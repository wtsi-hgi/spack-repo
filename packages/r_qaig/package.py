# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQaig(RPackage):
	"""Automatic Item Generator for Quantitative Multiple-Choice Items

	A tool for automatic generation of sibling items from a parent item model defined by
           the user. It is an implementation of the process automatic item generation (AIG) focused
           on generating quantitative multiple-choice type of items (see Embretson, Kingston
           (2018) <doi:10.1111/jedm.12166>).
	"""
	
	homepage = "https://github.com/shubh-b/QAIG"
	cran = "QAIG" 

	version("0.1.7", md5="2778d89f297dd54663f756f251406839")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
