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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/qpcrNorm_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/qpcrNorm/qpcrNorm_1.60.0.tar.gz"]

	version("1.60.0", sha256="4cf961759d309f5f2c093ac92358f4120a2127a911410b569689e484f2905247")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
