# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirsea(RPackage):
	"""'MicroRNA' Set Enrichment Analysis

	The tools for 'MicroRNA Set Enrichment Analysis' can identify risk pathways(or prior gene sets) regulated by microRNA set in the context of microRNA expression data. (1) This package constructs a correlation profile of microRNA and pathways by the hypergeometric statistic test. The gene sets of pathways derived from the three public databases (Kyoto Encyclopedia of Genes and Genomes ('KEGG'); 'Reactome'; 'Biocarta') and the target gene sets of microRNA are provided by four databases('TarBaseV6.0'; 'mir2Disease'; 'miRecords'; 'miRTarBase';). (2) This package can quantify the change of correlation between microRNA for each pathway(or prior gene set) based on a microRNA expression data with cases and controls. (3) This package uses the weighted Kolmogorov-Smirnov statistic to calculate an enrichment score (ES) of a microRNA set that co-regulate to a pathway , which reflects the degree to which a given pathway is associated with the specific phenotype. (4) This package can provide the visualization of the results.
	"""
	
	cran = "MiRSEA" 

	version("1.1.1", md5="0dc84e638e97bd341977b69f3202bd89")

	depends_on("r@2.15.1:", type=("build", "run"))
