# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocsi(RPackage):
	"""Receiver Operating Characteristic Based Signature Identification

	Optimal linear combination predictive signatures for maximizing the area between two Receiver Operating Characteristic (ROC) curves (treatment vs. control).
	"""
	
	cran = "ROCSI" 

	version("0.1.0", md5="e652ca2fcd58e4549315aa33c4bc1207")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
