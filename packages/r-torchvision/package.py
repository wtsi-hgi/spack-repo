# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTorchvision(RPackage):
	"""Models, Datasets and Transformations for Images

	Provides access to datasets, models and preprocessing
    facilities for deep learning with images. Integrates seamlessly
    with the 'torch' package and it's 'API' borrows heavily from
    'PyTorch' vision package.
	"""
	
	homepage = "https://torchvision.mlverse.org"
	cran = "torchvision" 

	version("0.5.1", md5="57074c4f1dbc519bbe7f86f7932021aa")

	depends_on("r-torch@0.5:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
