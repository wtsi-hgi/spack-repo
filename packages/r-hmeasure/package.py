# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmeasure(RPackage):
	"""The H-Measure and Other Scalar Classification Performance
Metrics

	Classification performance metrics that are derived from the ROC
    curve of a classifier. The package includes the H-measure performance metric
    as described in <http://link.springer.com/article/10.1007/s10994-009-5119-5>,
    which computes the minimum total misclassification cost, integrating over any
    uncertainty about the relative misclassification costs, as per a user-defined
    prior. It also offers a one-stop-shop for other scalar metrics of performance,
    including sensitivity, specificity and many others, and also offers plotting
    tools for ROC curves and related statistics.
	"""
	
	homepage = "http://www.hmeasure.net"
	cran = "hmeasure" 

	version("1.0-2", md5="f9e5a09f8faea5967d0350639b5fdb6a")

	depends_on("r@2.10:", type=("build", "run"))
