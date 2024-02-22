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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/eiR_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/eiR/eiR_1.42.0.tar.gz"]

	version("1.42.0", md5="71e5c96821411e053b417fb15618e1cb")

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
