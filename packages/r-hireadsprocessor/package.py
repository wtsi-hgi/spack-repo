# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHireadsprocessor(RPackage):
	"""Functions to process LM-PCR reads from 454/Illumina data

	hiReadsProcessor contains set of functions which allow users to process LM-PCR products sequenced using any platform. Given an excel/txt file containing parameters for demultiplexing and sample metadata, the functions automate trimming of adaptors and identification of the genomic product. Genomic products are further processed for QC and abundance quantification.
	"""
	
	bioc = "hiReadsProcessor" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/hiReadsProcessor_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/hiReadsProcessor/hiReadsProcessor_1.38.0.tar.gz"]

	version("1.38.0", sha256="ba8924a92f80f6aefa9f64070d5806428c15bd8430410ffdc94de54130246f36")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-hiannotator", type=("build", "run"))
	depends_on("r-soniclength", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
