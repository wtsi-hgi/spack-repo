# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElisatools(RPackage):
	"""ELISA Data Analysis with Batch Correction

	To run data analysis for enzyme-link immunosorbent assays (ELISAs). 
	Either the five- or four-parameter logistic model will be fitted for data of single ELISA. 
	Moreover, the batch effect correction/normalization will be carried out, when there are more than one batches of ELISAs. 
	Feng (2018) <doi:10.1101/483800>.
	"""
	
	cran = "ELISAtools" 

	version("0.1.5", md5="8b42591959a0a5fc654914639d55be9f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-r2html@2.3.2:", type=("build", "run"))
	depends_on("r-stringi@1.1.7:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2.1:", type=("build", "run"))
