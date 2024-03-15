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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/cfToolsData_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/cfToolsData/cfToolsData_1.0.0.tar.gz"]

	version("1.0.0", md5="00bbf328a45fb8731b3c7262b3521e0b")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

	# experiment