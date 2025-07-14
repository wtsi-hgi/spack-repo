# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsmooth(RPackage):
	"""Smooth quantile normalization

	Smooth quantile normalization is a generalization of quantile normalization, which is average of the two types of assumptions about the data generation process: quantile normalization and quantile normalization between groups.
	"""
	
	bioc = "qsmooth" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/qsmooth_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/qsmooth/qsmooth_1.18.0.tar.gz"]

    version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="e1bc687f8648f435e26e8b343241a19c17acb150c145fb5e179bcfc2414d8faf")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
