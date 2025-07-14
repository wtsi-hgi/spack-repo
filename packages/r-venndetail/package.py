# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVenndetail(RPackage):
	"""A package for visualization and extract details

	A set of functions to generate high-resolution Venn,Vennpie plot,extract and combine details of these subsets with user datasets in data frame is available.
	"""
	
	homepage = "https://github.com/guokai8/VennDetail"
	bioc = "VennDetail" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/VennDetail_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/VennDetail/VennDetail_1.18.0.tar.gz"]

    version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="b9eb5781c29e9d24a539dcf671b4f79aba8952538762612a911252711b888327")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
