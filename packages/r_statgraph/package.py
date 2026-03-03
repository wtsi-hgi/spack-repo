# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatgraph(RPackage):
	"""Statistical Methods for Graphs

	Contains statistical methods to analyze graphs, such as graph parameter estimation, 
    model selection based on the Graph Information Criterion, statistical tests to discriminate two or more populations of graphs, 
    correlation between graphs, and clustering of graphs.
    References: Takahashi et al. (2012) <doi:10.1371/journal.pone.0049949>, Fujita et al. (2017) <doi:10.3389/fnins.2017.00066>,
    Fujita et al. (2017) <doi:10.1016/j.csda.2016.11.016>, Tang et al. (2017) <doi:10.3150/15-BEJ789>,
    Tang et al. (2017) <doi:10.1080/10618600.2016.1193505>, Ghoshdastidar et al. (2017) <arXiv:1705.06168>,
    Ghoshdastidar et al. (2017) <arXiv:1707.00833>, Cerqueira et al. (2017) <doi:10.1109/TNSE.2017.2674026>,
    Fraiman and Fraiman (2018) <doi:10.1038/s41598-018-23152-5>, Fujita et al. (2019) <doi:10.1093/comnet/cnz028>.
	"""
	
	homepage = "https://www.ime.usp.br/~fujita/software.html"
	cran = "statGraph" 

	version("0.5.1", md5="e45e088b441c0c22bc0296d79c45ed8c")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
