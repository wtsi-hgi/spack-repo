# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGhap(RPackage):
	"""Genome-Wide Haplotyping

	Haplotype calling from phased marker data. Given user-defined haplotype blocks (HapBlock), the package identifies the different haplotype alleles (HapAllele) present in the data and scores sample haplotype allele genotypes (HapGenotype) based on HapAllele dose (i.e. 0, 1 or 2 copies). The output is not only useful for analyses that can handle multi-allelic markers, but is also conveniently formatted for existing pipelines intended for bi-allelic markers. The package was first described in Bioinformatics by Utsunomiya et al. (2016, <doi:10.1093/bioinformatics/btw356>). Since the v2 release, the package provides functions for unsupervised and supervised detection of ancestry tracks. The methods implemented in these functions were described in an article published in Methods in Ecology and Evolution by Utsunomiya et al. (2020, <doi:10.1111/2041-210X.13467>). The source code for v3 was modified for improved performance and inclusion of new functionality, including analysis of unphased data, runs of homozygosity, sampling methods for virtual gamete mating, mixed model fitting and GWAS.
	"""
	
	cran = "GHap" 

	version("3.0.0", md5="99b8edee02c4b378677eb604d0895cea")

	depends_on("r-matrix@1.2.16:", type=("build", "run"))
	depends_on("r-pedigreemm@0.3.3:", type=("build", "run"))
	depends_on("r-sparseinv@0.1.3:", type=("build", "run"))
	depends_on("r-e1071@1.7.0.1:", type=("build", "run"))
	depends_on("r-class@7.3.15:", type=("build", "run"))
	depends_on("r-data-table@1.12.6:", type=("build", "run"))
	depends_on("r-stringi@1.7.6:", type=("build", "run"))
