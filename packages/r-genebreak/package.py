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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GeneBreak_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GeneBreak/GeneBreak_1.32.0.tar.gz"]

	version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="96175010901d8f63140a327cc74f4e388620ad38ffb5a0e2630008b2424253ef")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-qdnaseq", type=("build", "run"))
	depends_on("r-cghcall", type=("build", "run"))
	depends_on("r-cghbase", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
