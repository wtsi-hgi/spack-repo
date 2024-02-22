# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadviz(RPackage):
	"""Project Multidimensional Data in 2D Space

	An implementation of the radviz projection in R. It enables the visualization of
    multidimensional data while maintaining the relation to the original dimensions.
    This package provides functions to create and plot radviz projections, and a number of summary
    plots that enable comparison and analysis. For reference see Ankerst *et al.* (1996) 
    (<https://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.68.1811>) for original implementation, 
    see Di Caro *et al* (2012) (<https://link.springer.com/chapter/10.1007/978-3-642-13672-6_13>) 
    for the original method for dimensional anchor arrangements, see Demsar *et al.* (2007) 
    (<doi:10.1016/j.jbi.2007.03.010>) for the original Freeviz implementation.
	"""
	
	homepage = "https://github.com/yannabraham/Radviz"
	cran = "Radviz" 

	version("0.9.3", md5="789a1767413408826ce607bcbc717c22")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
