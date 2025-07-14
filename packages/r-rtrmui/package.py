# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtrmui(RPackage):
	"""A shiny user interface for rTRM

	This package provides a web interface to compute transcriptional regulatory modules with rTRM.
	"""
	
	homepage = "https://github.com/ddiez/rTRMui"
	bioc = "rTRMui"

	version("1.46.0", commit="718b5bc955440e91b7c7d635a67bef576da13377")
	version("1.40.0", commit="ef7cd27504e1f6c6c183a6762ea08e44d63f0eed")

	depends_on("r-shiny@0.9:", type=("build", "run"))
	depends_on("r-rtrm", type=("build", "run"))
	depends_on("r-motifdb", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
