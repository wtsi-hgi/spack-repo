# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTargetsearch(RPackage):
	"""A package for the analysis of GC-MS metabolite profiling data

	This packages provides a flexible, fast and accurate method for targeted pre-processing of GC-MS data. The user provides a (often very large) set of GC chromatograms and a metabolite library of targets. The package will automatically search those targets in the chromatograms resulting in a data matrix that can be used for further data analysis.
	"""
	
	homepage = "https://github.com/acinostroza/TargetSearch"
	bioc = "TargetSearch" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TargetSearch_2.4.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TargetSearch/TargetSearch_2.4.2.tar.gz"]

	version("2.4.2", md5="7013b00950e240fcd7d53f0173d337e9")

	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
