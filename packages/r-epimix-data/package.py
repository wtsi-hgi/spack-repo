# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpimixData(RPackage):
	"""Data for the EpiMix package

	Supporting data for the EpiMix R package. It include: - HM450_lncRNA_probes.rda - HM450_miRNA_probes.rda - EPIC_lncRNA_probes.rda - EPIC_miRNA_probes.rda - EpigenomeMap.rda - LUAD.sample.annotation - TCGA_BatchData - MET.data - mRNA.data - microRNA.data - lncRNA.data - Sample_EpiMixResults_lncRNA - Sample_EpiMixResults_miRNA - Sample_EpiMixResults_Regular - Sample_EpiMixResults_Enhancer - lncRNA expression data of tumors from TCGA that are stored in the ExperimentHub.
	"""
	
	bioc = "EpiMix.data"

	version("1.10.0", commit="14ef6c9a4c7b15eca04f82b9c7d86c7a9484fad5")
	version("1.4.0", commit="6c2b70c286d8d95fbf9edea769230cc59e2b4ab8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-experimenthub@0.99.6:", type=("build", "run"))

