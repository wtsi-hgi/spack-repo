# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCystisim(RPackage):
	"""Agent-Based Model for Taenia_solium Transmission and Control

	The cystiSim package provides an agent-based model for Taenia solium transmission and control. cystiSim was developed within the framework of CYSTINET, the European Network on taeniosis/cysticercosis, COST ACTION TD1302.
	"""
	
	homepage = "https://github.com/brechtdv/cystiSim"
	cran = "cystiSim" 

	version("0.1.0", md5="df4f50628a08516935abcf6160980152")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
