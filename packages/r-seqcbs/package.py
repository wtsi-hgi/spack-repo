# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqcbs(RPackage):
	"""Copy Number Profiling using Sequencing and CBS

	This is a method for DNA Copy Number Profiling using
        Next-Generation Sequencing. It has new model and test
        statistics based on non-homogeneous Poisson Processes with
        change point models. It uses an adaptation of Circular Binary
        Segmentation. Also included are methods for point-wise Bayesian
        Confidence Interval and model selection method for the
        change-point model. A case and a control sample reads (normal
        and tumor) are required.
	"""
	
	cran = "seqCBS" 

	version("1.2.1", md5="e7ff2c93bde14edecc774eed74e03778")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
