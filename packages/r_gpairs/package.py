# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpairs(RPackage):
	"""The Generalized Pairs Plot

	Offers a generalization of the scatterplot matrix based on the recognition that most datasets include both categorical and quantitative information. Traditional grids of scatterplots often obscure important features of the data when one or more variables are categorical but coded as numerical. The generalized pairs plot offers a range of displays of paired combinations of categorical and quantitative variables. Emerson et al. (2013) <DOI:10.1080/10618600.2012.694762>.
	"""
	
	cran = "gpairs" 

	version("1.3.3", md5="6fe8863fb930a60f948bb12dee624a10")

	depends_on("r-barcode", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
