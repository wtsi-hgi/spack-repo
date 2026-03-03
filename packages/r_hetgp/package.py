# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHetgp(RPackage):
	"""Heteroskedastic Gaussian Process Modeling and Design under
Replication

	Performs Gaussian process regression with heteroskedastic noise following the model by Binois, M., Gramacy, R., Ludkovski, M. (2016) <arXiv:1611.05902>, with implementation details in Binois, M. & Gramacy, R. B. (2021) <doi:10.18637/jss.v098.i13>. The input dependent noise is modeled as another Gaussian process. Replicated observations are encouraged as they yield computational savings. Sequential design procedures based on the integrated mean square prediction error and lookahead heuristics are provided, and notably fast update functions when adding new observations.
	"""
	
	cran = "hetGP" 

	version("1.1.6", md5="eab672fcd17e0fa3d6799fe5808b9c37")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dicedesign", type=("build", "run"))
