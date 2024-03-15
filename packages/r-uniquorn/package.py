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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Uniquorn_2.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Uniquorn/Uniquorn_2.22.0.tar.gz"]

	version("2.22.0", md5="63658e23af6991784cdd4b038f2d1268")

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
