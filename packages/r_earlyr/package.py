# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REarlyr(RPackage):
	"""Estimation of Transmissibility in the Early Stages of a Disease
Outbreak

	Implements a simple, likelihood-based estimation of the reproduction number (R0) using a branching process with a Poisson likelihood. This model requires knowledge of the serial interval distribution, and dates of symptom onsets. Infectiousness is determined by weighting R0 by the probability mass function of the serial interval on the corresponding day. It is a simplified version of the model introduced by Cori et al. (2013) <doi:10.1093/aje/kwt133>.
	"""
	
	homepage = "https://www.repidemicsconsortium.org/earlyR/"
	cran = "earlyR" 

	version("0.0.5", md5="610768a5337eb09e7570a73e75d7ce86")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-distcrete", type=("build", "run"))
	depends_on("r-epiestim", type=("build", "run"))
	depends_on("r-epitrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
