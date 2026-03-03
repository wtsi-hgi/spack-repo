# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedigree(RPackage):
	"""Pedigree Functions

	Pedigree related functions.
	"""
	
	cran = "pedigree" 

	version("1.4.2", md5="b4a177fda9dc578665dfc201abb4f398")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-haplosim@1.8.4:", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
