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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rTRMui_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rTRMui/rTRMui_1.40.0.tar.gz"]

	version("1.40.0", sha256="b5df627bc08009197727a4d5e176636a001a9536436bf8be68199a852b3fe2ce")

	depends_on("r-shiny@0.9:", type=("build", "run"))
	depends_on("r-rtrm", type=("build", "run"))
	depends_on("r-motifdb", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
