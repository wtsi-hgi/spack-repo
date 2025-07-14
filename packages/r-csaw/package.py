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

	version("1.42.0", commit="5e3afe7c670bd02f7e7e2e50b14baa59d6c90175")
	version("1.36.1", commit="25b51baa26f9c935d97ba4b48055e75c55d191f7")

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
