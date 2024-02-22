# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfhub(RPackage):
	"""Interface to 'TensorFlow' Hub

	'TensorFlow' Hub is a library for the publication, discovery, and
    consumption of reusable parts of machine learning models. A module is a 
    self-contained piece of a 'TensorFlow' graph, along with its weights and 
    assets, that can be reused across different tasks in a process known as
    transfer learning. Transfer learning train a model with a smaller dataset,
    improve generalization, and speed up training.
	"""
	
	homepage = "https://github.com/rstudio/tfhub"
	cran = "tfhub" 

	version("0.8.1", md5="014188b66828c197b8661c9c68c7ba29")

	depends_on("r-reticulate@1.9.0.9002:", type=("build", "run"))
	depends_on("r-tensorflow@1.8.0.9006:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("py-tensorflow@2.0:", type=("build", "link", "run"))
