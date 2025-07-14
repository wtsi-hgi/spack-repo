# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbqn(RPackage):
	"""Mean/Median-balanced quantile normalization

	Modified quantile normalization for omics or other matrix-like data distorted in location and scale.
	"""
	
	homepage = "https://github.com/arianeschad/mbqn"
	bioc = "MBQN" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MBQN_2.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MBQN/MBQN_2.14.0.tar.gz"]

	version("2.20.0", tag="RELEASE_3_21")
	version("2.14.0", sha256="a213de3bcc0021cdead31da732236962433e347e7e0066343ed91589c34a1e6a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-limma@3.30.13:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.10:", type=("build", "run"))
	depends_on("r-preprocesscore@1.36:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-paireddata", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
