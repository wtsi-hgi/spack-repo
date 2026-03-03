# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvivalroc(RPackage):
	"""Time-Dependent ROC Curve Estimation from Censored Survival Data

	Compute time-dependent ROC curve from censored survival
        data using Kaplan-Meier (KM) or Nearest Neighbor Estimation
        (NNE) method of Heagerty, Lumley & Pepe (Biometrics, Vol 56 No
        2, 2000, PP 337-344).
	"""
	
	cran = "survivalROC" 

	version("1.0.3.1", md5="f902d8d1d91cbed98b43ca3cfb9cddaa")

	depends_on("r@1.6.1:", type=("build", "run"))
