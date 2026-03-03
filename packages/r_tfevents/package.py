# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfevents(RPackage):
	"""Write Events for 'TensorBoard'

	Provides a convenient way to log scalars, images, audio, and histograms in the 'tfevent' record file format. 
  Logged data can be visualized on the fly using 'TensorBoard', a web based tool that focuses on visualizing the training 
  progress of machine learning models.
	"""
	
	homepage = "https://github.com/mlverse/tfevents"
	cran = "tfevents" 

	version("0.0.2", md5="3b8049fc38a8cb42d30747d995a01a23")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-blob", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
	depends_on("protobuf", type=("build", "link", "run"))
