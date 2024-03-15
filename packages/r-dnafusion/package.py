# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnafusion(RPackage):
	"""Identification of gene fusions using paired-end sequencing

	DNAfusion can identify gene fusions such as EML4-ALK based on paired-end sequencing results. This package was developed using position deduplicated BAM files generated with the AVENIO Oncology Analysis Software. These files are made using the AVENIO ctDNA surveillance kit and Illumina Nextseq 500 sequencing. This is a targeted hybridization NGS approach and includes ALK-specific but not EML4-specific probes.
	"""
	
	homepage = "https://github.com/CTrierMaansson/DNAfusion"
	bioc = "DNAfusion" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DNAfusion_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DNAfusion/DNAfusion_1.4.0.tar.gz"]

	version("1.4.0", md5="b7ef2bb10bea5334d6d159208c284c16")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-bamsignals", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-biocbaseutils", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
