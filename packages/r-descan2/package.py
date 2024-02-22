# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescan2(RPackage):
	"""Differential Enrichment Scan 2

	Integrated peak and differential caller, specifically designed for broad epigenomic signals.
	"""
	
	bioc = "DEScan2" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DEScan2_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DEScan2/DEScan2_1.22.0.tar.gz"]

	version("1.22.0", md5="476f052d4a86e27d332812852fd7e0c1", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/DEScan2_1.22.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-chippeakanno", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors@0.23.19:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
