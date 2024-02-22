# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParglms(RPackage):
	"""support for parallelized estimation of GLMs/GEEs

	This package provides support for parallelized estimation of GLMs/GEEs, catering for dispersed data.
	"""
	
	bioc = "parglms" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/parglms_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/parglms/parglms_1.34.0.tar.gz"]

	version("1.34.0", md5="0d6a2dc756389064b9be38e755e1a24b")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-batchjobs", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
