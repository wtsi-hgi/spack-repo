# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbm2sas(RPackage):
	"""Convert GBM Object Trees to SAS Code

	Writes SAS code to get predicted values from every tree of a gbm.object.
	"""
	
	cran = "gbm2sas" 

	version("3.0", md5="3866ce8edad3f21d4faf562c84e462b3")

	depends_on("r-gbm", type=("build", "run"))
