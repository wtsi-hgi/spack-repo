# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAloom(RPackage):
	"""All Leave-One-Out Models

	Creates all leave-one-out models and produces predictions for test samples.
	"""
	
	homepage = "https://www.rcc.org.rs/aloom.html"
	cran = "aloom" 

	version("0.1.1", md5="f66773ec4d9b280190c96e9908c18ec9")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
