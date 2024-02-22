# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH2o4gpu(RPackage):
	"""Interface to 'H2O4GPU'

	Interface to 'H2O4GPU' <https://github.com/h2oai/h2o4gpu>, a collection of 'GPU' solvers for machine learning algorithms.
	"""
	
	homepage = "https://github.com/h2oai/h2o4gpu"
	cran = "h2o4gpu" 

	version("0.3.3", md5="446ce80315827c9466173d9a696d6f04")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reticulate@1.4:", type=("build", "run"))
	depends_on("python@3.6:", type=("build", "link", "run"))
