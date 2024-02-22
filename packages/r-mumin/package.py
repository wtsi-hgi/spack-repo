# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMumin(RPackage):
	"""Multi-Model Inference

	Tools for performing model selection and model averaging. Automated
             model selection through subsetting the maximum model, with optional
             constraints for model inclusion. Model parameter and prediction
             averaging based on model weights derived from information criteria
             (AICc and alike) or custom model weighting schemes.
	"""
	
	cran = "MuMIn" 

	version("1.47.5", md5="e733ab93b8e3cff6e827c04634f54976")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
