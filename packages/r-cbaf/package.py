# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbaf(RPackage):
	"""Automated functions for comparing various omic data from cbioportal.org

	This package contains functions that allow analysing and comparing omic data across various cancers/cancer subgroups easily. So far, it is compatible with RNA-seq, microRNA-seq, microarray and methylation datasets that are stored on cbioportal.org.
	"""
	
	bioc = "cbaf" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cbaf_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cbaf/cbaf_1.24.0.tar.gz"]

    version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="119afd78a65b81bc4a5788ccf5878e9a737b950f4f6ecb70ee690931d08ec8fc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-cbioportaldata", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
