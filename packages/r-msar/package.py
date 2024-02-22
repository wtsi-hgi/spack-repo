# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsar(RPackage):
	"""Multiple Sequence Alignment for R Shiny

	Visualizes multiple sequence alignments dynamically within the
    Shiny web application framework.
	"""
	
	cran = "msaR" 

	version("0.6.0", md5="b3d5eac5f5d14336a2b83d5bcbf4b310")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
