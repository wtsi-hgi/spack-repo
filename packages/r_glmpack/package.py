# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmpack(RPackage):
	"""Data and Code to Accompany Generalized Linear Models, 2nd
Edition

	Contains all the data and functions used in Generalized
    Linear Models, 2nd edition, by Jeff Gill and Michelle Torres. Examples to create
    all models, tables, and plots are included for each data set.
	"""
	
	cran = "GLMpack" 

	version("0.1.0", md5="34d81f48e5a621b6aa1671f6425cf851")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbrackets", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-effects", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-censreg", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
