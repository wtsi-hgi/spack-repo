# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlinkqc(RPackage):
	"""Genotype Quality Control with 'PLINK'

	Genotyping arrays enable the direct measurement of an individuals
    genotype at thousands of markers. 'plinkQC' facilitates genotype quality
    control for genetic association studies as described by Anderson and
    colleagues (2010) <doi:10.1038/nprot.2010.116>. It makes 'PLINK' basic
    statistics (e.g. missing genotyping rates per individual, allele frequencies
    per genetic marker) and relationship functions accessible from 'R' and
    generates a per-individual and per-marker quality control report.
    Individuals and markers that fail the quality control can subsequently be
    removed to generate a new, clean dataset. Removal of individuals based on
    relationship status is optimised to retain as many individuals as possible
    in the study.
	"""
	
	homepage = "https://meyer-lab-cshl.github.io/plinkQC/"
	cran = "plinkQC" 

	version("0.3.4", md5="16e164a51443765195a74e8ae53254cb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-optparse", type=("build", "run"))
	depends_on("r-data-table@1.11:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph@1.2.4:", type=("build", "run"))
	depends_on("r-sys", type=("build", "run"))
	depends_on("plink@1.9:", type=("build", "link", "run"))
