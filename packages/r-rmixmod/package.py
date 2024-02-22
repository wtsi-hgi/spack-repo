# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmixmod(RPackage):
	"""Classification with Mixture Modelling

	Interface of 'MIXMOD' software for supervised, unsupervised and
    semi-supervised classification with mixture modelling <doi: 10.18637/jss.v067.i06>.
	"""
	
	cran = "Rmixmod" 

	version("2.1.10", md5="38db0fd33a09fc2496c9e0ae66b76547")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
