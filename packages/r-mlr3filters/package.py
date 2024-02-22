# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3filters(RPackage):
	"""Filter Based Feature Selection for 'mlr3'

	Extends 'mlr3' with filter methods for feature selection.
    Besides standalone filter methods built-in methods of any
    machine-learning algorithm are supported.  Partial scoring of
    multivariate filter methods is supported.
	"""
	
	homepage = "https://mlr3filters.mlr-org.com"
	cran = "mlr3filters" 

	version("0.7.1", md5="d56d5686a5b5dac1d8ea0beaecb56790")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mlr3@0.12:", type=("build", "run"))
	depends_on("r-mlr3misc", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
