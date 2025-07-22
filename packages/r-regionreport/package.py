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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/regionReport_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/regionReport/regionReport_1.36.0.tar.gz"]

	version("1.36.0", sha256="676e65645afe51b9d5c639529fc0f5d1f16ee90ef3c4fd5322e76c67cc4c71da")

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
