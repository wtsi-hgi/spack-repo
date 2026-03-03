# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTgst(RPackage):
	"""Targeted Gold Standard Testing

	Functions for implementing the targeted gold standard (GS) testing. You provide the true disease or treatment failure status and the risk score, tell 'TGST' the availability of GS tests and which method to use, and it returns the optimal tripartite rules. Please refer to Liu et al. (2013) <doi:10.1080/01621459.2013.810149> for more details.
	"""
	
	cran = "TGST" 

	version("1.0", md5="487a84027de20a880d512ac23b144b88")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
