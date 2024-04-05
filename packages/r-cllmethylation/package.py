# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCllmethylation(RPackage):
	"""Methylation data of primary CLL samples in PACE project

	The package includes DNA methylation data for the primary Chronic Lymphocytic Leukemia samples included in the Primary Blood Cancer Encyclopedia (PACE) project. Raw data from the 450k DNA methylation arrays is stored in the European Genome-Phenome Archive (EGA) under accession number EGAS0000100174. For more information concerning the project please refer to the paper "Drug-perturbation-based stratification of blood cancer" by Dietrich S, Oles M, Lu J et al., J. Clin. Invest. (2018) and R/Bioconductor package BloodCancerMultiOmics2017.
	"""
	
	bioc = "CLLmethylation" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/CLLmethylation_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/CLLmethylation/CLLmethylation_1.22.0.tar.gz"]

	version("1.22.0", md5="a8c3768dca1df5bb9e911878b68ad4c4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

