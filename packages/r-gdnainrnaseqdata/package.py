# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdnainrnaseqdata(RPackage):
	"""RNA-seq data with different levels of gDNA contamination

	Provides access to BAM files generated from RNA-seq data produced with different levels of gDNA contamination. It currently allows one to download a subset of the data published by Li et al., BMC Genomics, 23:554, 2022. This subset of data is formed by BAM files with about 100,000 alignments with three different levels of gDNA contamination.
	"""
	
	homepage = "https://github.com/functionalgenomics/gDNAinRNAseqData"
	bioc = "gDNAinRNAseqData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/gDNAinRNAseqData_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/gDNAinRNAseqData/gDNAinRNAseqData_1.2.0.tar.gz"]

	version("1.2.0", sha256="887fb03e45da8cbb10d1924c34e8cccc4e2815ae0a815f58bfb386c56123618f")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))

