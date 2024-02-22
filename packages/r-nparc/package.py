# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNparc(RPackage):
	"""Non-parametric analysis of response curves for thermal proteome profiling experiments

	Perform non-parametric analysis of response curves as described by Childs, Bach, Franken et al. (2019): Non-parametric analysis of thermal proteome profiles reveals novel drug-binding proteins.
	"""
	
	bioc = "NPARC" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/NPARC_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/NPARC/NPARC_1.14.0.tar.gz"]

	version("1.14.0", md5="b49f408fb60e58d3c62cfd2d5d4809cb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
