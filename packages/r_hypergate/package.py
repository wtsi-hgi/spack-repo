# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHypergate(RPackage):
	"""Machine Learning of Hyperrectangular Gating Strategies for
High-Dimensional Cytometry

	Given a high-dimensional dataset that typically represents a cytometry dataset, and a subset of the datapoints, this algorithm outputs an hyperrectangle so that datapoints within the hyperrectangle best correspond to the specified subset. In essence, this allows the conversion of clustering algorithms' outputs to gating strategies outputs.
	"""
	
	cran = "hypergate" 

	version("0.8.5", md5="d899de98c9e7c4ca6a6c067e96d8123a")

	depends_on("r@3.5:", type=("build", "run"))
