# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmpbam(RPackage):
	"""C++ Library for OpenMP-based multi-threaded sequential profiling of Binary Alignment Map (BAM) files

	This packages provides C++ header files for developers wishing to create R packages that processes BAM files. ompBAM automates file access, memory management, and handling of multiple threads 'behind the scenes', so developers can focus on creating domain-specific functionality. The included vignette contains detailed documentation of this API, including quick-start instructions to create a new ompBAM-based package, and step-by-step explanation of the functionality behind the example packaged included within ompBAM.
	"""
	
	homepage = "https://github.com/alexchwong/ompBAM"
	bioc = "ompBAM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ompBAM_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ompBAM/ompBAM_1.6.0.tar.gz"]

	version("1.6.0", md5="9e9d31ddcad0b4bb4acb30ad970a0cd5")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
