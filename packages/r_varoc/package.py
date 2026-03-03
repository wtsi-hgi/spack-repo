# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVaroc(RPackage):
	"""Value Added Receiver Operating Characteristics Curve

	A continuous version of the receiver operating characteristics (ROC) curve to visualize and assess the classification and continuity performances of biomarkers, diagnostic tests, or risk prediction models.
	"""
	
	cran = "varoc" 

	version("0.2.0", md5="47819aa1c91497cfad5d7480a85f6019")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
