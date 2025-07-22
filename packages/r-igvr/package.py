# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgvr(RPackage):
	"""igvR: integrative genomics viewer

	Access to igv.js, the Integrative Genomics Viewer running in a web browser.
	"""
	
	homepage = "https://gladkia.github.io/igvR/"
	bioc = "igvR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/igvR_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/igvR/igvR_1.22.0.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="b38e44b5638f2a141657c7ec0d9ac763672c32fd8dd3c41ed06f4a266fa45132")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-browserviz@2.17.1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
