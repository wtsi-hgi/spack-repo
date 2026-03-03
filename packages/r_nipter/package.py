# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNipter(RPackage):
	"""Fast and Accurate Trisomy Prediction in Non-Invasive Prenatal
Testing

	Fast and Accurate Trisomy Prediction in Non-Invasive Prenatal
    Testing.
	"""
	
	cran = "NIPTeR" 

	version("1.0.2", md5="7184014a0e47fa302ed3f5763f8a4db2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
