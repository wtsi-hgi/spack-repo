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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NPARC_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NPARC/NPARC_1.14.0.tar.gz"]

	version("1.14.0", sha256="30f5fb942d09d1f4fa653245c97c49a50acd51c544040c155d113a382bcc9f04")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
