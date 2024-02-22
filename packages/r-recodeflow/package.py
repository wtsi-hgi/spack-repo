# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecodeflow(RPackage):
	"""Interface Functions for PMML Creation, and Data Recoding

	Contains functions to interface with variables and variable details sheets, including recoding variables and converting them to PMML.
	"""
	
	homepage = "https://github.com/Big-Life-Lab/recodeflow"
	cran = "recodeflow" 

	version("0.1.0", md5="15cb27048e78ab860f05dfd956d21853")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-xml@3.98.1.11:", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
