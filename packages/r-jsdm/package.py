# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsdm(RPackage):
	"""Joint Species Distribution Models

	Fits joint species distribution models ('jSDM')
    in a hierarchical Bayesian framework (Warton and al. 2015
    <doi:10.1016/j.tree.2015.09.007>). The Gibbs sampler is written
    in 'C++'. It uses 'Rcpp', 'Armadillo' and 'GSL' to maximize computation
    efficiency.
	"""
	
	homepage = "https://ecology.ghislainv.fr/jSDM/"
	cran = "jSDM" 

	version("0.2.6", md5="c569d194895694bda94124d7282f06e4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
