# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMimager(RPackage):
	"""mimager: The Microarray Imager

	Easily visualize and inspect microarrays for spatial artifacts.
	"""
	
	homepage = "https://github.com/aaronwolen/mimager"
	bioc = "mimager" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mimager_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mimager/mimager_1.26.0.tar.gz"]

	version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="107645249ccea58eacc26c90cfa8a4405889d81d720edb60f89abfbc5e991c03")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-affyplm", type=("build", "run"))
	depends_on("r-oligo", type=("build", "run"))
	depends_on("r-oligoclasses", type=("build", "run"))
