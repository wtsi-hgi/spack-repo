# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQpcrnorm(RPackage):
	"""Data-driven normalization strategies for high-throughput qPCR data.

	The package contains functions to perform normalization of high-throughput qPCR data. Basic functions for processing raw Ct data plus functions to generate diagnostic plots are also available.
	"""
	
	bioc = "qpcrNorm" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/qpcrNorm_1.60.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/qpcrNorm/qpcrNorm_1.60.0.tar.gz"]

	version("1.60.0", md5="43fa513309301e6d8e89fcef668c7b28")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
