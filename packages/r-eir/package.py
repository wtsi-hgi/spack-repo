# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REir(RPackage):
	"""Accelerated similarity searching of small molecules

	The eiR package provides utilities for accelerated structure similarity searching of very large small molecule data sets using an embedding and indexing approach.
	"""
	
	homepage = "https://github.com/girke-lab/eiR"
	bioc = "eiR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/eiR_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/eiR/eiR_1.42.0.tar.gz"]

	version("1.42.0", sha256="53c2812540a22b06579982e97f96894b6fd3b2a8abc8d1119572a0161b68e443")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-chemminer", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rcppannoy@0.0.9:", type=("build", "run"))
