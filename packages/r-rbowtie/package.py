# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbowtie(RPackage):
	"""R bowtie wrapper

	This package provides an R wrapper around the popular bowtie short read aligner and around SpliceMap, a de novo splice junction discovery and alignment tool. The package is used by the QuasR bioconductor package. We recommend to use the QuasR package instead of using Rbowtie directly.
	"""
	
	homepage = "https://github.com/fmicompbio/Rbowtie"
	bioc = "Rbowtie"

	version("1.48.0", commit="3e162af88b4acc0a89bcf9b3309569b02dc840c6")
	version("1.42.0", commit="bd0120f019e17bd52306046e58447a8398af2476")

	depends_on("zlib", type=("build", "link", "run"))
