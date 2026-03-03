# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexvarjm(RPackage):
	"""Estimate Joint Models with Subject-Specific Variance

	Estimation of mixed models including a subject-specific variance which can be time and covariate dependent. In the joint model framework, the package handles left truncation and allows a flexible dependence structure between the competing events and the longitudinal marker. The estimation is performed under the frequentist framework, using the Marquardt-Levenberg algorithm. (Courcoul, Tzourio, Woodward, Barbieri, Jacqmin-Gadda (2023) <arXiv:2306.16785>).
	"""
	
	homepage = "https://github.com/LeonieCourcoul/FlexVarJM"
	cran = "FlexVarJM" 

	version("0.1.0", md5="d7424a1d8371db665090cdb8eb568683")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lcmm", type=("build", "run"))
	depends_on("r-marqlevalg", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
