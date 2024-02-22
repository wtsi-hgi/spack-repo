# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCummerbund(RPackage):
	"""Analysis, exploration, manipulation, and visualization of Cufflinks high-throughput sequencing data.

	Allows for persistent storage, access, exploration, and manipulation of Cufflinks high-throughput sequencing data.  In addition, provides numerous plotting functions for commonly used visualizations.
	"""
	
	bioc = "cummeRbund" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/cummeRbund_2.44.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/cummeRbund/cummeRbund_2.44.0.tar.gz"]

	version("2.44.0", md5="367d124a098eca55a6da149e35621c65")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
