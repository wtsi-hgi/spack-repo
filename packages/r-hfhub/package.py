# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHfhub(RPackage):
	"""Hugging Face Hub Interface

	Provides functionality to download and cache files from 'Hugging Face Hub' <https://huggingface.co/models>. 
    Uses the same caching structure so files can be shared between different client libraries.
	"""
	
	homepage = "https://mlverse.github.io/hfhub/"
	cran = "hfhub" 

	version("0.1.1", md5="1aeea81e34b03a5f0e04b7a91d3bb3c3")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-filelock", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
