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

	version("1.42.0", md5="409fc50371b1eaf9be2af500aff05249")

	depends_on("zlib", type=("build", "link", "run"))

	def setup_build_environment(self, env):
		env.append_path("CPATH", self.spec["zlib"].prefix.include)
