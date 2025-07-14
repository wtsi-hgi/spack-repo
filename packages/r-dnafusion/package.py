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

	version("1.10.0", commit="052b16ccd86a278982ba3c0a3962ee7dd39983f9")
	version("1.4.0", commit="6684cb77ddbd7d6171e1f213f7d74b9ba5a57b7c")

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
