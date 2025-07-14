# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvmetrics(RPackage):
	"""Copy Number Variant Metrics

	The CNVMetrics package calculates similarity metrics to facilitate copy number variant comparison among samples and/or methods. Similarity metrics can be employed to compare CNV profiles of genetically unrelated samples as well as those with a common genetic background. Some metrics are based on the shared amplified/deleted regions while other metrics rely on the level of amplification/deletion. The data type used as input is a plain text file containing the genomic position of the copy number variations, as well as the status and/or the log2 ratio values. Finally, a visualization tool is provided to explore resulting metrics.
	"""
	
	homepage = "https://github.com/krasnitzlab/CNVMetrics"
	bioc = "CNVMetrics" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CNVMetrics_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CNVMetrics/CNVMetrics_1.6.0.tar.gz"]

	version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="95db84f879b5726ae2389ee54bafc8966fa9aeb9bf3c65cd4ffbdb665823c49a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rbeta2009", type=("build", "run"))
