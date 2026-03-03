# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPewdata(RPackage):
	"""Reproducible Retrieval of Pew Research Center Datasets

	Reproducible, programmatic retrieval of survey datasets from the
    Pew Research Center.
	"""
	
	homepage = "https://github.com/fsolt/pewdata"
	cran = "pewdata" 

	version("0.3.2", md5="0b4884089dcc62867ff8a5f8d6d082cc")

	depends_on("r-rselenium", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
