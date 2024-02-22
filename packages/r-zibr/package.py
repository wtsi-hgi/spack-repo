# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZibr(RPackage):
	"""A Zero-Inflated Beta Random Effect Model

	A two-part zero-inflated Beta regression model with random 
    effects (ZIBR) for testing the association between microbial abundance 
    and clinical covariates for longitudinal microbiome data. Eric Z. Chen 
    and Hongzhe Li (2016) <doi:10.1093/bioinformatics/btw308>.
	"""
	
	homepage = "https://github.com/PennChopMicrobiomeProgram/ZIBR"
	cran = "ZIBR" 

	version("1.0.2", md5="482b90d6055a20bcc9faa29a9dbb3e6c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
