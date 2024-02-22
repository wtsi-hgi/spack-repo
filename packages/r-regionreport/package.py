# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegionreport(RPackage):
	"""Generate HTML or PDF reports for a set of genomic regions or DESeq2/edgeR results

	Generate HTML or PDF reports to explore a set of regions such as the results from annotation-agnostic expression analysis of RNA-seq data at base-pair resolution performed by derfinder. You can also create reports for DESeq2 or edgeR results.
	"""
	
	homepage = "https://github.com/leekgroup/regionReport"
	bioc = "regionReport" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/regionReport_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/regionReport/regionReport_1.36.0.tar.gz"]

	version("1.36.0", md5="8ec5fb1e7db2235d543b2a9a6660a3b3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biocstyle@2.5.19:", type=("build", "run"))
	depends_on("r-derfinder@1.25.3:", type=("build", "run"))
	depends_on("r-deformats", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-knitr@1.6:", type=("build", "run"))
	depends_on("r-knitrbootstrap@0.9:", type=("build", "run"))
	depends_on("r-refmanager", type=("build", "run"))
	depends_on("r-rmarkdown@0.9.5:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
