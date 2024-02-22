# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTorchdatasets(RPackage):
	"""Ready to Use Extra Datasets for Torch

	Provides datasets in a format that can be easily consumed by torch 'dataloaders'.
  Handles data downloading from multiple sources, caching and pre-processing so
  users can focus only on their model implementations.
	"""
	
	homepage = "https://mlverse.github.io/torchdatasets/"
	cran = "torchdatasets" 

	version("0.3.0", md5="51a7441c4447b4afb0c280eef0b31b33")

	depends_on("r-torch@0.5:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-pins", type=("build", "run"))
	depends_on("r-torchvision", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
