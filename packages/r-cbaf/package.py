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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/cbaf_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/cbaf/cbaf_1.24.0.tar.gz"]

	version("1.24.0", md5="e3c093194c8fdcbd04ca035dddeaf5f5")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-cbioportaldata", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
