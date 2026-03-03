# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdmeasurer(RPackage):
	"""Assessment of Individual Identity in Animal Signals

	Provides tools for assessment and quantification of individual identity information in animal signals. This package accompanies a research article by Linhart et al. (2019) <doi:10.1101/546143>: "Measuring individual identity information in animal signals: Overview and performance of available identity metrics".
	"""
	
	cran = "IDmeasurer" 

	version("1.0.0", md5="424683e1dd82421331d5f3880aef3d12")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
