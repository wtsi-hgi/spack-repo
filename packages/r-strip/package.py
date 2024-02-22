# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrip(RPackage):
	"""Lighten your R Model Outputs

	The strip function deletes components of R model outputs that are useless for specific purposes, such as predict[ing], print[ing], summary[izing], etc.
	"""
	
	homepage = "https://github.com/paulponcet/strip"
	cran = "strip" 

	version("1.0.0", md5="b86d9e75fd16be155eafba7d0511a1aa")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
