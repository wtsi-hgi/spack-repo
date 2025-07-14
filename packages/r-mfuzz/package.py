# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfuzz(RPackage):
	"""Soft clustering of time series gene expression data

	Package for noise-robust soft clustering of gene expression time-series data (including a graphical user interface)
	"""
	
	homepage = "http://mfuzz.sysbiolab.eu/"
	bioc = "Mfuzz" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Mfuzz_2.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Mfuzz/Mfuzz_2.62.0.tar.gz"]

	version("2.68.0", tag="RELEASE_3_21")
	version("2.62.0", sha256="ee7e7a6134e8c2e945789940588e254f94e97231e22b5395eb348c91a21b546c")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-tkwidgets", type=("build", "run"))
