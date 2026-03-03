# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCommkern(RPackage):
	"""Network-Based Communities and Kernel Machine Methods

	Analysis of network community objects with applications to neuroimaging data. There are two main components to this package. The first is the hierarchical multimodal spinglass (HMS) algorithm, which is a novel community detection algorithm specifically tailored to the unique issues within brain connectivity. The other is a suite of semiparametric kernel machine methods that allow for statistical inference to be performed to test for potential associations between these community structures and an outcome of interest (binary or continuous).
	"""
	
	homepage = "https://github.com/aljensen89/CommKern"
	cran = "CommKern" 

	version("1.0.1", md5="6932361469a3a331c8e069708c3647bf")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
