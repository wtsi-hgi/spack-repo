# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCascade(RPackage):
	"""Selection, Reverse-Engineering and Prediction in Cascade
Networks

	A modeling tool allowing gene selection, reverse engineering, and prediction in cascade networks. Jung, N., Bertrand, F., Bahram, S., Vallat, L., and Maumy-Bertrand, M. (2014) <doi:10.1093/bioinformatics/btt705>.
	"""
	
	homepage = "https://fbertran.github.io/Cascade/"
	cran = "Cascade" 

	version("2.1", md5="ae94a55ffd963f0a0910794f3b79bf84")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tnet", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
