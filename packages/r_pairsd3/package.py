# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPairsd3(RPackage):
	"""D3 Scatterplot Matrices

	Creates an interactive scatterplot matrix using the D3 JavaScript
    library. See <https://d3js.org/> for more information on D3.
	"""
	
	homepage = "https://github.com/garthtarr/pairsD3/"
	cran = "pairsD3" 

	version("0.1.3", md5="04cb9afcb5a7646fe3393646f9e1b1d9", url="https://cran.r-project.org/src/contrib/pairsD3_0.1.3.tar.gz")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.3.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
