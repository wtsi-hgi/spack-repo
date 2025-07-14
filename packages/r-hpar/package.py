# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpar(RPackage):
	"""Human Protein Atlas in R

	The hpar package provides a simple R interface to and data from the Human Protein Atlas project.
	"""
	
	bioc = "hpar"

	version("1.50.0", commit="9173bc2981acd71c8acb5931e53fb7c17d85de8f")
	version("1.44.0", commit="c1f5902fd7dcc8238815105de610246ba855ff50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
