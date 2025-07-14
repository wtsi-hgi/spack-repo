# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaqcsubsetilm(RPackage):
	"""MAQC data subset for the Illumina platform

	MAQC data subset for the Illumina platform
	"""
	
	bioc = "MAQCsubsetILM"

	version("1.40.0", commit="9030acadeb63c2747e913a978c21ca5ac2c8b3b2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))

