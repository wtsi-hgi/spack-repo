# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNricens(RPackage):
	"""NRI for Risk Prediction Models with Time to Event and Binary
Response Data

	Calculating the net reclassification improvement (NRI) for risk prediction models with time to event and binary data.
	"""
	
	cran = "nricens" 

	version("1.6", md5="ed4d23ac5be6fcaefd247cc21318c126")

	depends_on("r-survival", type=("build", "run"))
