# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecombinator(RPackage):
	"""Recombinate Nested Lists to Dataframes

	Turns nested lists into data.frames in an orderly manner.
	"""
	
	cran = "recombinator" 

	version("1.0.1", md5="9d2d1a3aa7d52199661e3b1207357ac7")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
