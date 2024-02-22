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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rTRMui_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rTRMui/rTRMui_1.40.0.tar.gz"]

	version("1.40.0", md5="6e1589a0f3e51870f4eb71a0eb56d915")

	depends_on("r-shiny@0.9:", type=("build", "run"))
	depends_on("r-rtrm", type=("build", "run"))
	depends_on("r-motifdb", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
