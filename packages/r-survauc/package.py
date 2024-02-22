# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvauc(RPackage):
	"""Estimators of Prediction Accuracy for Time-to-Event Data

	Provides a variety of functions to estimate
        time-dependent true/false positive rates and AUC curves from a
        set of censored survival data.
	"""
	
	cran = "survAUC" 

	version("1.2-0", md5="add65be25058104abb0a2d9ef818a87a")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
