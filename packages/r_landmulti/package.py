# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLandmulti(RPackage):
	"""Landmark Prediction with Multiple Short-Term Events

	Contains functions for a flexible varying-coefficient landmark model by incorporating multiple short-term events into the prediction of long-term survival probability. For more information about landmark prediction please see Li, W., Ning, J., Zhang, J., Li, Z., Savitz, S.I., Tahanan, A., Rahbar.M.H., (2023+). "Enhancing Long-term Survival Prediction with Multiple Short-term Events: Landmarking with A Flexible Varying Coefficient Model".
	"""
	
	cran = "landmulti" 

	version("0.5.0", md5="da37f118f8c6ceebaa6fb52165cdaead")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-landpred", type=("build", "run"))
	depends_on("r-nmof", type=("build", "run"))
	depends_on("r-emdbook", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
