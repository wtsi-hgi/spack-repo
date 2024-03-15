# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbwa(RPackage):
	"""R wrapper for BWA-backtrack and BWA-MEM aligners

	Provides an R wrapper for BWA alignment algorithms. Both BWA-backtrack and BWA-MEM are available. Convenience function to build a BWA index from a reference genome is also provided. Currently not supported for Windows machines.
	"""
	
	homepage = "https://github.com/Jfortin1/Rbwa"
	bioc = "Rbwa" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rbwa_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rbwa/Rbwa_1.6.0.tar.gz"]

	version("1.6.0", md5="036e0acc237e1249e5509df62d6c9968")

	depends_on("r@4.1:", type=("build", "run"))
