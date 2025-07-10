# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaskbad(RPackage):
	"""Masking probes with binding affinity differences

	Package includes functions to analyze and mask microarray expression data.
	"""
	
	bioc = "maskBAD" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/maskBAD_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/maskBAD/maskBAD_1.46.0.tar.gz"]

	version("1.46.0", sha256="bef451a8de2f5fbece91b4dd03dfeeba6fb62bf5a71c539d7e4c8b14a9227986")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gcrma@2.27.1:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
