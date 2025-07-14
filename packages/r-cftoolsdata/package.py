# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCftoolsdata(RPackage):
	"""ExperimentHub data for the cfTools package

	The cfToolsData package supplies the data for the cfTools package. It contains two pre-trained deep neural network (DNN) models for the cfSort function. Additionally, it includes the shape parameters of beta distribution characterizing methylation markers associated with four tumor types for the CancerDetector function, as well as the parameters characterizing methylation markers specific to 29 primary human tissue types for the cfDeconvolve function.
	"""
	
	homepage = "https://github.com/jasminezhoulab/cfToolsData"
	bioc = "cfToolsData"

	version("1.6.0", commit="e46e1947d1450c1189bd87c8437019706bc6a8fb")
	version("1.0.0", commit="62944016dc4ea28f54c48ae990152aedfd64cc1d")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

