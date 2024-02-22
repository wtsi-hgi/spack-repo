# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgbiplot(RPackage):
	"""A Grammar of Graphics Implementation of Biplots

	A 'ggplot2' based implementation of biplots, giving a representation of a dataset in
    a two dimensional space accounting for the greatest variance, together with variable vectors
    showing how the data variables relate to this space. It provides a 
    replacement for stats::biplot(), but with many enhancements to control the analysis and
    graphical display. It implements 
    biplot and scree plot methods which can be used with the results of prcomp(), princomp(),
    FactoMineR::PCA(), ade4::dudi.pca() or MASS::lda() and can be customized using 'ggplot2' techniques.
	"""
	
	homepage = "https://github.com/friendly/ggbiplot"
	cran = "ggbiplot" 

	version("0.6.2", md5="ad05e753b93a1c517462240db51731d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
