# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrpc(RPackage):
	"""PC Algorithm with the Principle of Mendelian Randomization

	A PC Algorithm with the Principle of Mendelian Randomization. This package implements the MRPC 
            (PC with the principle of Mendelian randomization) algorithm to infer causal graphs. It also 
            contains functions to simulate data under a certain topology, to visualize a graph in different 
            ways, and to compare graphs and quantify the differences. 
            See Badsha and Fu (2019) <doi:10.3389/fgene.2019.00460>,Badsha, Martin and Fu (2021) <doi:10.3389/fgene.2021.651812>. 
	"""
	
	cran = "MRPC" 

	version("3.1.0", md5="f95981a3004543713c1027f1f7b55344")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
