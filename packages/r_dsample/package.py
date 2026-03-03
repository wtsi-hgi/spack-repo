# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsample(RPackage):
	"""Discretization-Based Direct Random Sample Generation

	Discretization-based random sampling algorithm that is useful for a complex model in high dimension is implemented. The normalizing constant of a target distribution is not needed. Posterior summaries are compared with those by 'OpenBUGS'. The method is described: Wang and Lee (2014) <doi:10.1016/j.csda.2013.06.011> and exercised in Lee (2009) <http://hdl.handle.net/1993/21352>.
	"""
	
	cran = "dsample" 

	version("0.91.3.4", md5="4f4868c86df4ffa046706592ce8e50a0")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
