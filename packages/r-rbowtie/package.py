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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rbowtie_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rbowtie/Rbowtie_1.42.0.tar.gz"]

	version("1.42.0", sha256="88a2aaa3bbbc451aae708d5ba88e39a2ddbee9709029daf94aaf301d1fca3cab")

	depends_on("zlib", type=("build", "link", "run"))
