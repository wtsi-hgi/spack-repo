# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniquorn(RPackage):
	"""Identification of cancer cell lines based on their weighted mutational/ variational fingerprint

	'Uniquorn' enables users to identify cancer cell lines. Cancer cell line misidentification and cross-contamination reprents a significant challenge for cancer researchers. The identification is vital and in the frame of this package based on the locations/ loci of somatic and germline mutations/ variations. The input format is vcf/ vcf.gz and the files have to contain a single cancer cell line sample (i.e. a single member/genotype/gt column in the vcf file).
	"""
	
	bioc = "Uniquorn"

	version("2.28.0", commit="5c491bdea6031e3566a4787828bd3a73f639aa47")
	version("2.22.0", commit="207ec1c98530f1576fc47a6371cde0e8fd64add6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-writexls", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
