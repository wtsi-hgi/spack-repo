# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFksum(RPackage):
	"""Fast Kernel Sums

	Implements the method of Hofmeyr, D.P. (2021) <DOI:10.1109/TPAMI.2019.2930501> for fast evaluation of univariate kernel smoothers based on recursive computations.
  Applications to the basic problems of density and regression function estimation are provided, as well as some projection pursuit methods
  for which the objective is based on non-parametric functionals of the projected density, or conditional density of a response given projected
  covariates.
  The package is accompanied by an instructive paper in the Journal of Statistical Software <doi:10.18637/jss.v101.i03>.
	"""
	
	cran = "FKSUM" 

	version("1.0.1", md5="fbce5dc1f19ac2015892a204454ff148")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
