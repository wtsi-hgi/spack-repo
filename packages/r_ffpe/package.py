# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFfpe(RPackage):
	"""Quality assessment and control for FFPE microarray expression data

	Identify low-quality data using metrics developed for expression data derived from Formalin-Fixed, Paraffin-Embedded (FFPE) data.  Also a function for making Concordance at the Top plots (CAT-plots).
	"""
	
	bioc = "ffpe" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ffpe_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ffpe/ffpe_1.46.0.tar.gz"]

	version("1.46.0", md5="c2a3dbd53e85caf82d7c8f91a8277454")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))
	depends_on("r-methylumi", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
