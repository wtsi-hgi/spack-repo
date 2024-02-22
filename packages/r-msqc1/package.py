# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsqc1(RPackage):
	"""Sigma mix MSQC1 data

	contains eight technical replicate data set and a three replicate dilution series of the MS Qual/Quant Quality Control Mix standard sample (Sigma-Aldrich, Buchs, Switzerland) measured on five different mass spectrometer platforms at the Functional Genomics Center Zurich.
	"""
	
	homepage = "https://panoramaweb.org/labkey/MSQC1.url"
	bioc = "msqc1" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/msqc1_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/msqc1/msqc1_1.30.0.tar.gz"]

	version("1.30.0", md5="a95a760a0c0ef5e8053acee1d59170a4", url="https://www.bioconductor.org/packages/release/data/experiment/src/contrib/msqc1_1.30.0.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))

	# experiment