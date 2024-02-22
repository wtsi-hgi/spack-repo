# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapassoc(RPackage):
	"""Inference of Trait Associations with SNP Haplotypes and Other
Attributes using the EM Algorithm

	The following R functions are used for inference of trait
        associations with haplotypes and other covariates in
        generalized linear models.  The functions are developed
        primarily for data collected in cohort or cross-sectional
        studies. They can accommodate uncertain haplotype phase and
        handle missing genotypes at some SNPs.
	"""
	
	homepage = "https://sfustatgen.github.io/research/hapassoc.html"
	cran = "hapassoc" 

	version("1.2-9", md5="daefc0cf50b718e1ac017da1b581c9b2")

	depends_on("r@2.6:", type=("build", "run"))
