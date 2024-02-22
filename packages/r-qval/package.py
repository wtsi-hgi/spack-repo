# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQval(RPackage):
	"""The Q-Matrix Validation Methods Framework

	Provide a variety of Q-matrix validation methods for the generalized cognitive diagnosis models, including the method based on the generalized deterministic input, noisy, “and” gate model (G-DINA) by de la Torre (2011) <DOI:10.1007/s11336-011-9207-7> discrimination index (the GDI method) by de la Torre and Chiu (2016) <DOI:10.1007/s11336-015-9467-8>, the step-wise Wald test method (the Wald method) by Ma and de la Torre (2020) <DOI:10.1111/bmsp.12156>, the Hull method by Najera et al. (2021) <DOI:10.1111/bmsp.12228>, the  multiple logistic regression‑based Q‑matrix validation method  (the MLR-B method) by Tu et al. (2022) <DOI:10.3758/s13428-022-01880-x>. Different research methods during Q-matrix validating are available.
	"""
	
	cran = "Qval" 

	version("0.1.4", md5="4d49099dfd953a40713569ec301dc6ea")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gdina", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
