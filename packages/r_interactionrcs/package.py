# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteractionrcs(RPackage):
	"""Calculate Estimates in Models with Interaction

	A tool to calculate and plot estimates from models 
    in which an interaction between the main predictor and a continuous covariate has been specified.
    Methods used in the package refer to Harrell Jr FE (2015, ISBN:9783319330396); 
    Durrleman S, Simon R. (1989) <doi:10.1002/sim.4780080504>; Greenland S. (1995) <doi:10.1097/00001648-199507000-00005>.
	"""
	
	cran = "interactionRCS" 

	version("0.1.1", md5="a51e695563500cef9a1d8af39fceb799")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-pspline", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
