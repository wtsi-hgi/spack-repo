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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/parglms_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/parglms/parglms_1.34.0.tar.gz"]

	version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="c15ecb94c622db80ff689ff3ea44f487f8176180c2ba004e0594b37c5bb3b916")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-batchjobs", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
