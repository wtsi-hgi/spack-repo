# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcsclust(RPackage):
	"""Tandem Clustering with Invariant Coordinate Selection

	Implementation of tandem clustering with invariant coordinate 
              selection with different scatter matrices and several choices for the 
              selection of components as described in Alfons, A., Archimbaud, A., Nordhausen, K.and Ruiz-Gazen, A. (2022) <arXiv:2212.06108>.
	"""
	
	homepage = "https://github.com/AuroreAA/ICSClust"
	cran = "ICSClust" 

	version("0.1.0", md5="5f2c5492ad1ed7155ed5dc4e5dcbfd63")

	depends_on("r-ics@1.4.0:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-heplots", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-otrimle", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tclust", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
