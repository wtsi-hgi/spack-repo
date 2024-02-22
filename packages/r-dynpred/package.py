# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynpred(RPackage):
	"""Companion Package to "Dynamic Prediction in Clinical Survival
Analysis"

	The dynpred package contains functions for dynamic prediction in survival analysis.
	"""
	
	homepage = "http://www.msbi.nl/putter"
	cran = "dynpred" 

	version("0.1.2", md5="06b198abdb47b28ba561194b9095e620")

	depends_on("r-survival", type=("build", "run"))
