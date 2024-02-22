# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDinamicDuo(RPackage):
	"""Finding Recurrent DNA Copy Number Alterations and Differences

	In tumor tissue, underlying genomic instability can lead to DNA copy number alterations,
	e.g., copy number gains or losses. Sporadic copy number alterations occur randomly throughout the
	genome, whereas recurrent alterations are observed in the same genomic region across multiple
	independent samples, perhaps because they provide a selective growth advantage. Here we use
	cyclic shift permutations to identify recurrent copy number alterations in a single cohort or
	recurrent copy number differences in two cohorts based on a common set of genomic markers.
	Additional functionality is provided to perform downstream analyses, including the creation of
	summary files and graphics. DiNAMIC.Duo builds upon the original DiNAMIC package of Walter et al.
	(2011) <doi:10.1093/bioinformatics/btq717> and leverages the theory developed in Walter et al.
	(2015) <doi:10.1093/biomet/asv046>. An article describing DiNAMIC.Duo by Walter et al. (2022)
	can be found at <doi: 10.1093/bioinformatics/btac542>.
	"""
	
	cran = "DiNAMIC.Duo" 

	version("1.0.2", md5="4f6cc9f1250c682120598c3c2b90b67a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-dinamic", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("python", type=("build", "link", "run"))
	depends_on("py-numpy", type=("build", "link", "run"))
