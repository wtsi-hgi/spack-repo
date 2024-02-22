# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtas(RPackage):
	"""Modeling Earthquake Data Using 'ETAS' Model

	Fits the space-time Epidemic Type Aftershock Sequence
    ('ETAS') model to earthquake catalogs using a stochastic 'declustering' 
    approach. The 'ETAS' model is a 'spatio-temporal' marked point process
    model and a special case of the 'Hawkes' process. The package is based 
    on a Fortran program by 'Jiancang Zhuang'
    (available at <http://bemlar.ism.ac.jp/zhuang/software.html>),
    which is modified and translated into C++ and C such that it 
    can be called from R. Parallel computing with 'OpenMP' is possible 
    on supported platforms.
	"""
	
	homepage = "https://github.com/jalilian/ETAS"
	cran = "ETAS" 

	version("0.5.1", md5="cf30d9873b3064b7a8d8ef72699ec90d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-goftest", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
