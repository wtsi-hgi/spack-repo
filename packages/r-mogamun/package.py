# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogamun(RPackage):
	"""MOGAMUN: A Multi-Objective Genetic Algorithm to Find Active Modules in Multiplex Biological Networks

	MOGAMUN is a multi-objective genetic algorithm that identifies active modules in a multiplex biological network. This allows analyzing different biological networks at the same time. MOGAMUN is based on NSGA-II (Non-Dominated Sorting Genetic Algorithm, version II), which we adapted to work on networks.
	"""
	
	homepage = "https://github.com/elvanov/MOGAMUN"
	bioc = "MOGAMUN" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MOGAMUN_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MOGAMUN/MOGAMUN_1.12.0.tar.gz"]

	version("1.12.0", sha256="5b51e64f55440860de7d285938afb84e669106859d7478999c1e9e565557fc74")

	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
