# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovsim(RPackage):
	"""VITA, IG and PLSIM Simulation for Given Covariance and Marginals

	Random sampling from distributions with user-specified population covariance matrix. Marginal information may be fully
        specified, for which the package implements the VITA (VIne-To-Anything) algorithm
        Grønneberg and Foldnes (2017) <doi:10.1007/s11336-017-9569-6>.  See also Grønneberg, Foldnes and Marcoulides (2022) <doi:10.18637/jss.v102.i03>.
        Alternatively, marginal skewness and kurtosis may be specified, for which the package
        implements the IG (independent generator) and PLSIM (piecewise linear) algorithms, see Foldnes and Olsson (2016) <doi:10.1080/00273171.2015.1133274> and
        Foldnes and Grønneberg (2021) <doi:10.1080/10705511.2021.1949323>, respectively.  
	"""
	
	cran = "covsim" 

	version("1.0.0", md5="814dedc5e0c2703b1fe8cead273d7f10")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rvinecopulib@0.5.1.1:", type=("build", "run"))
	depends_on("r-lavaan@0.6.5:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-pearsonds", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
