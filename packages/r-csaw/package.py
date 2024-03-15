# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsaw(RPackage):
	"""ChIP-Seq Analysis with Windows

	Detection of differentially bound regions in ChIP-seq data with sliding windows, with methods for normalization and proper FDR control.
	"""
	
	bioc = "csaw" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/csaw_1.36.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/csaw/csaw_1.36.1.tar.gz"]

	version("1.36.1", md5="8872d08420c497718f401b6c10f30ebc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-metapod", type=("build", "run"))
	depends_on("r-rhtslib", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
