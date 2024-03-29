# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoolfstat(RPackage):
	"""Computing f-Statistics and Building Admixture Graphs Based on
Allele Count or Pool-Seq Read Count Data

	Functions for the computation of f- and D-statistics (estimation of 'Fst', Patterson's 'F2', 'F3', 'F3*', 'F4' and D parameters) in population genomics studies from allele count or Pool-Seq read count data and for the fitting, building and visualization of admixture graphs. The package also includes several utilities to manipulate Pool-Seq data stored in standard format (e.g., such as 'vcf' files or 'rsync' files generated by the the 'PoPoolation' software) and perform conversion to alternative format (as used in the 'BayPass' and 'SelEstim' software). As of version 2.0, the package also includes utilities to manipulate standard allele count data (e.g., stored in 'TreeMix', 'BayPass' or 'SelEstim' format).
	"""
	
	cran = "poolfstat" 

	version("2.2.0", md5="701cf103ce1d41ce2b9eaf58e5bafa94")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ryacas", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
