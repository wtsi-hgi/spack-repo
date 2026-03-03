# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBradleyterry2(RPackage):
	"""Bradley-Terry Models

	Specify and fit the Bradley-Terry model, including structured versions in which the parameters are related to explanatory variables through a linear predictor and versions with contest-specific effects, such as a home advantage.
	"""
	
	homepage = "https://github.com/hturner/BradleyTerry2"
	cran = "BradleyTerry2" 

	version("1.1-2", md5="9fd6564a39782270813e111cb0293726", url="https://cran.r-project.org/src/contrib/BradleyTerry2_1.1-2.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-brglm", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-lme4@1:", type=("build", "run"))
	depends_on("r-qvcalc", type=("build", "run"))
