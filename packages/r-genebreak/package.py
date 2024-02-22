# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenebreak(RPackage):
	"""Gene Break Detection

	Recurrent breakpoint gene detection on copy number aberration profiles.
	"""
	
	homepage = "https://github.com/stefvanlieshout/GeneBreak"
	bioc = "GeneBreak" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GeneBreak_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GeneBreak/GeneBreak_1.32.0.tar.gz"]

	version("1.32.0", md5="32b69bf4150c25c908235217dc805ed3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-qdnaseq", type=("build", "run"))
	depends_on("r-cghcall", type=("build", "run"))
	depends_on("r-cghbase", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
