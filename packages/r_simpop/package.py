# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimpop(RPackage):
	"""Simulation of Complex Synthetic Data Information

	Tools and methods to simulate populations for surveys based
    on auxiliary data. The tools include model-based methods, calibration and
    combinatorial optimization algorithms, see Templ, Kowarik and Meindl (2017) <doi:10.18637/jss.v079.i10>) and
    Templ (2017) <doi:10.1007/978-3-319-50272-4>. The package was developed with support of
    the International Household Survey Network, DFID Trust Fund TF011722 and funds
    from the World bank.
	"""
	
	homepage = "https://github.com/statistikat/simPop"
	cran = "simPop" 

	version("2.1.3", md5="69730f1f5f040cf3684cd17027d04c8c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-vim", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-wrswor", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
