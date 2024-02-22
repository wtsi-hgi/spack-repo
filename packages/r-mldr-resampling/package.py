# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMldrResampling(RPackage):
	"""Resampling Algorithms for Multi-Label Datasets

	Collection of the state of the art multi-label resampling algorithms. The objective of these algorithms is to achieve balance in multi-label datasets.
	"""
	
	cran = "mldr.resampling" 

	version("0.2.3", md5="a8855ddb4cba4048094bb45340af04af")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mldr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-vecsets", type=("build", "run"))
