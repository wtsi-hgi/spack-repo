# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellity(RPackage):
	"""Quality Control for Single-Cell RNA-seq Data

	A support vector machine approach to identifying and filtering low quality cells from single-cell RNA-seq datasets.
	"""
	
	bioc = "cellity"

	version("1.36.0", commit="868299ef5ce230ca79dd0d9d91724df22e95d680")
	version("1.30.0", commit="7cff628b1b90a10390da77c21854c9469195f8a1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvoutlier", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
