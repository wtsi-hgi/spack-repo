# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpcmlasso(RPackage):
	"""Differential Item Functioning in Generalized Partial Credit
Models

	Provides a framework to detect Differential Item Functioning (DIF) in Generalized Partial Credit Models (GPCM) and special cases of the GPCM as proposed by Schauberger and Mair (2019) <doi:10.3758/s13428-019-01224-2>. A joint model is set up where DIF is explicitly parametrized and penalized likelihood estimation is used for parameter selection. The big advantage of the method called GPCMlasso is that several variables can be treated simultaneously and that both continuous and categorical variables can be used to detect DIF.
	"""
	
	cran = "GPCMlasso" 

	version("0.1-7", md5="dd5d23af0af514dc2d9fe6ae01d546c0")

	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
