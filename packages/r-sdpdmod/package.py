# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdpdmod(RPackage):
	"""Spatial Dynamic Panel Data Modeling

	Spatial model calculation for static and dynamic panel data models, weights matrix creation and  Bayesian model comparison.
  Bayesian model comparison methods were described by 'LeSage' (2014) <doi:10.1016/j.spasta.2014.02.002>.
  The 'Lee'-'Yu' transformation approach is described in 'Yu', 'De Jong' and 'Lee' (2008) <doi:10.1016/j.jeconom.2008.08.002>, 'Lee' and 'Yu' (2010) <doi:10.1016/j.jeconom.2009.08.001> and 'Lee' and 'Yu' (2010) <doi:10.1017/S0266466609100099>.
	"""
	
	cran = "SDPDmod" 

	version("0.0.3", md5="5a6d2ba961f73a8e6bf22018d5a50b66")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
