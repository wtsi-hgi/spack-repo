# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicdistributionsdata(RPackage):
	"""Reference data for GenomicDistributions package

	This package provides ready to use reference data for GenomicDistributions package. Raw data was obtained from ensembldb and processed with helper functions. Data files are available for the following genome assemblies: hg19, hg38, mm9 and mm10.
	"""
	
	bioc = "GenomicDistributionsData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/GenomicDistributionsData_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/GenomicDistributionsData/GenomicDistributionsData_1.10.0.tar.gz"]

	version("1.10.0", sha256="8449600cfb5dc96275185dc7298ffd732cdeba3172d0a5ff07a85e6b5bc537b1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub@1.14:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-annotationfilter", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))

