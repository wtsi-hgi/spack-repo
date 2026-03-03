# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayfoxr(RPackage):
	"""Global Bayesian Foraminifera Core Top Calibration

	A Bayesian, global planktic foraminifera core top calibration to 
    modern sea-surface temperatures. Includes four calibration models, 
    considering species-specific calibration parameters and seasonality.
	"""
	
	homepage = "https://github.com/brews/bayfoxr/"
	cran = "bayfoxr" 

	version("0.0.1", md5="05a3aa35224f8098c2cbd61142e131f1")

	depends_on("r@3.4:", type=("build", "run"))
