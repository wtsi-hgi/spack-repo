# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFindpc(RPackage):
	"""findPC is a software tool including six methods to automatically select the number of principal components to retain based on the standard deviations explained by each PC."""
	
	homepage = "https://github.com/haotian-zhuang/findPC"
	git = "https://github.com/haotian-zhuang/findPC.git"

	version("2022-06-27", commit="0e85c94124a4dd6037b4fecb0558450b0301b512")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
