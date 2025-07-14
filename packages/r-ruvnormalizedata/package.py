# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuvnormalizedata(RPackage):
	"""Gender data for the RUVnormalize package

	Microarray gene expression data from the study of Vawter et al., 2004.
	"""
	
	bioc = "RUVnormalizeData"

	version("1.28.0", commit="c880da15348dd6ea604176b374617113e18b5b74")
	version("1.22.0", commit="36f1957234bee83d07d160d9dd52ab303d8cad8b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

