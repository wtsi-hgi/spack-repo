# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetspanel(RPackage):
	"""General-to-Specific Modelling of Panel Data

	Uses several types of indicator saturation and automated General-to-Specific (GETS) modelling from the 'gets' package and applies it to panel data. This allows the detection of structural breaks in panel data, operationalising a reverse causal approach of causal inference, see Pretis and Schwarz (2022) <doi:10.2139/ssrn.4022745>.
	"""
	
	homepage = "https://github.com/moritzpschwarz/getspanel"
	cran = "getspanel" 

	version("0.1.5", md5="03029ce1fd2a861099ebc010020723c9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gets", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
