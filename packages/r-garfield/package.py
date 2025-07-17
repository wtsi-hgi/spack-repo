# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGarfield(RPackage):
    """GWAS Analysis of Regulatory or Functional Information Enrichment with LD correction

    GARFIELD is a non-parametric functional enrichment analysis approach described in the paper GARFIELD: GWAS analysis of regulatory or functional information enrichment with LD correction. Briefly, it is a method that leverages GWAS findings with regulatory or functional annotations (primarily from ENCODE and Roadmap epigenomics data) to find features relevant to a phenotype of interest. It performs greedy pruning of GWAS SNPs (LD r2 > 0.1) and then annotates them based on functional information overlap. Next, it quantifies Fold Enrichment (FE) at various GWAS significance cutoffs and assesses them by permutation testing, while matching for minor allele frequency, distance to nearest transcription start site and number of LD proxies (r2 > 0.8).
    """

    bioc = "garfield"

    version("1.36.0", commit="1fb080377421b8b190ad5cf415f1b727303f105e")
    version("1.30.0", commit="3366e6b083241e7afdb68ff817bb327347a293a8")
