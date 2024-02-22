# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtorch(RPackage):
	"""R Bindings to 'PyTorch'

	'R' implementation and interface of the Machine Learning platform 
    'PyTorch' <https://pytorch.org/> developed in 'Python'. It requires a 'conda'
    environment with 'torch' and 'torchvision' Python packages to provide 
    'PyTorch' functions, methods and classes. The key object in 'PyTorch' is the 
    tensor which is in essence a multidimensional array. These tensors are fairly 
    flexible in performing calculations in CPUs as well as 'GPUs' to accelerate 
    tensor operations.
	"""
	
	homepage = "https://github.com/f0nzie/rTorch"
	cran = "rTorch" 

	version("0.4.2", md5="f8cc6b5e16ee15f01619e31c59c7c846")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-reticulate@1.10:", type=("build", "run"))
	depends_on("r-jsonlite@1.2:", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
	depends_on("py-torch@1.4:", type=("build", "link", "run"))
	depends_on("py-torchvision", type=("build", "link", "run"))
	depends_on("py-numpy", type=("build", "link", "run"))
	depends_on("pandoc@2.0:", type=("build", "link", "run"))
	depends_on("python@3.6:", type=("build", "link", "run"))
