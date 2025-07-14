# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuvnormalize(RPackage):
	"""RUV for normalization of expression array data

	RUVnormalize is meant to remove unwanted variation from gene expression data when the factor of interest is not defined, e.g., to clean up a dataset for general use or to do any kind of unsupervised analysis.
	"""
	
	bioc = "RUVnormalize"

	version("1.42.0", commit="342e8bc186c5864e3785bbabbfbf1765deffc92b")
	version("1.36.0", commit="16236e946ad5424a61ae3b25a4ba067baed4d00c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ruvnormalizedata", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
