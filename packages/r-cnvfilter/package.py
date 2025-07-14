# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvfilter(RPackage):
	"""Identifies false positives of CNV calling tools by using SNV calls

	CNVfilteR identifies those CNVs that can be discarded by using the single nucleotide variant (SNV) calls that are usually obtained in common NGS pipelines.
	"""
	
	homepage = "https://github.com/jpuntomarcos/CNVfilteR"
	bioc = "CNVfilteR"

	version("1.22.0", commit="efef6b477c4fdd965b123f0329d7ab91e2850378")
	version("1.16.0", commit="b3a6913f647b6b64adfa9a148cb915c87ddd1e4c")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-regioner", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-karyoploter", type=("build", "run"))
	depends_on("r-copynumberplots", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
