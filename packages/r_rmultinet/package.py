# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmultinet(RPackage):
	"""Multi-Layer Networks Analysis

	Provides two general frameworks to generate a multi-layer network. This also provides several methods to reveal the embedding of both nodes and layers. The reference paper can be found from the URL mentioned below. Ting Li, Zhongyuan Lyu, Chenyu Ren, Dong Xia (2023) <arXiv:2302.04437>.
	"""
	
	cran = "rMultiNet" 

	version("0.1", md5="5b674a7f7a951dc7293be9ecb9983505")

	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-geigen", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
