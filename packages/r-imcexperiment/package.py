# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImcexperiment(RPackage):
	"""Mass Cytometry S4 Class Structure Pipeline for Images

	Containerizes cytometry data and allows for S4 class structure to extend slots related to cell morphology, spatial coordinates, phenotype network information, and unique cellular labeling.
	"""
	
	cran = "imcExperiment" 

	version("0.99.0", md5="70fbfef602e3a9990fb55cd2e8a5e8fc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
