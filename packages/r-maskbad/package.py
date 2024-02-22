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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/maskBAD_1.46.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/maskBAD/maskBAD_1.46.0.tar.gz"]

	version("1.46.0", md5="a5fc8482a4370f32fde7bc2b3e302c77")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gcrma@2.27.1:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
