# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigfuge(RPackage):
	"""SigFuge

	Algorithm for testing significance of clustering in RNA-seq data.
	"""
	
	bioc = "SigFuge"

	version("1.46.0", commit="c969487f6a547f6bb0dbcb9d3c47a4b7d7315ef9")
	version("1.40.0", commit="bcbafbccd76a561043bc0b822e3c0012e2f8c149")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-sigclust", type=("build", "run"))
