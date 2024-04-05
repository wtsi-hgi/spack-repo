# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcwlpipelines(RPackage):
	"""Bioinformatics pipelines based on Rcwl

	A collection of Bioinformatics tools and pipelines based on R and the Common Workflow Language.
	"""
	
	bioc = "RcwlPipelines" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RcwlPipelines_1.18.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RcwlPipelines/RcwlPipelines_1.18.1.tar.gz"]

	version("1.18.1", md5="807f999489f242a052fee4a11a5c27d3")
	version("1.18.0", md5="5ff1c2848694b09cc639a56009392cf3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcwl", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
