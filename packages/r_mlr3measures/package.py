# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3measures(RPackage):
	"""Performance Measures for 'mlr3'

	Implements multiple performance measures for
    supervised learning.  Includes over 40 measures for regression and
    classification. Additionally, meta information about the performance
    measures can be queried, e.g. what the best and worst possible
    performances scores are.
	"""
	
	homepage = "https:///mlr3measures.mlr-org.com"
	cran = "mlr3measures" 

	version("0.5.0", md5="84850fc10a9b3c352efe1e3d40bc1e39")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-prroc", type=("build", "run"))
