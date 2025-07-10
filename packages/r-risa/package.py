# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRisa(RPackage):
	"""Converting experimental metadata from ISA-tab into Bioconductor data structures

	The Investigation / Study / Assay (ISA) tab-delimited format is a general purpose framework with which to collect and communicate complex metadata (i.e. sample characteristics, technologies used, type of measurements made) from experiments employing a combination of technologies, spanning from traditional approaches to high-throughput techniques. Risa allows to access metadata/data in ISA-Tab format and build Bioconductor data structures. Currently, data generated from microarray, flow cytometry and metabolomics-based (i.e. mass spectrometry) assays are supported. The package is extendable and efforts are undergoing to support metadata associated to proteomics assays.
	"""
	
	homepage = "http://www.isa-tools.org/"
	bioc = "Risa" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Risa_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Risa/Risa_1.44.0.tar.gz"]

	version("1.44.0", sha256="58b0cbf8382040a2cc9842c870019e59285a3ee8f0784edf75ae1eaa49271890")

	depends_on("r@2.0.9:", type=("build", "run"))
	depends_on("r-biobase@2.4:", type=("build", "run"))
	depends_on("r-rcpp@0.9.13:", type=("build", "run"))
	depends_on("r-biocviews", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-xcms", type=("build", "run"))
