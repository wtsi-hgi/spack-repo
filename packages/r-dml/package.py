# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDml(RPackage):
	"""Distance Metric Learning in R

	The state-of-the-art algorithms for distance metric learning, including global and local methods such as Relevant Component Analysis, Discriminative Component Analysis, Local Fisher Discriminant Analysis, etc. These distance metric learning methods are widely applied in feature extraction, dimensionality reduction, clustering, classification, information retrieval, and computer vision problems.
	"""
	
	homepage = "https://github.com/terrytangyuan/dml"
	cran = "dml" 

	version("1.1.0", md5="57ee955143bd1552d4c4f16f52f0d68f")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lfda", type=("build", "run"))
