# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplifynet(RPackage):
	"""Network Sparsification

	Network sparsification with a variety of novel and known network sparsification 
    techniques. All network sparsification techniques reduce the number of edges, not the number 
    of nodes. Network sparsification is sometimes referred to as network dimensionality reduction. 
    This package is based on the work of Spielman, D., Srivastava, N. (2009)<arXiv:0803.0929>.
    Koutis I., Levin, A., Peng, R. (2013)<arXiv:1209.5821>. Toivonen, H., Mahler, S., Zhou, F. 
    (2010)<doi:10.1007>. Foti, N., Hughes, J., Rockmore, D. (2011)<doi:10.1371>.
	"""
	
	cran = "simplifyNet" 

	version("0.0.1", md5="8b2fd2ff8acca367810d0a7ca071d131")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-igraph@1.3.1:", type=("build", "run"))
	depends_on("r-sanic@0.0.1:", type=("build", "run"))
	depends_on("r-matrix@1.2.18:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
