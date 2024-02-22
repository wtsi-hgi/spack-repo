# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStroupglmm(RPackage):
	"""R Codes and Datasets for Generalized Linear Mixed Models: Modern
Concepts, Methods and Applications by Walter W. Stroup

	R Codes and Datasets for Stroup, W. W. (2012). Generalized Linear Mixed Models: Modern Concepts, Methods and Applications, CRC Press.
	"""
	
	homepage = "https://github.com/MYaseen208/StroupGLMM"
	cran = "StroupGLMM" 

	version("0.1.0", md5="9a51783e93e3ee6027fab61b00f043fc")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-lsmeans", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mutoss", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-pbkrtest", type=("build", "run"))
	depends_on("r-phia", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
