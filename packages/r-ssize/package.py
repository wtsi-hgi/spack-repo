# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsize(RPackage):
	"""Estimate Microarray Sample Size

	Functions for computing and displaying sample size information for gene expression arrays.
	"""
	
	bioc = "ssize" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ssize_1.76.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ssize/ssize_1.76.0.tar.gz"]

	version("1.82.0", tag="RELEASE_3_21")
	version("1.76.0", sha256="1cb6061432220cf41a857b05a8c0998ff4555c4fd862b8e0afbfb489250bc42e")

	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
