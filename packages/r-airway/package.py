# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirway(RPackage):
	"""RangedSummarizedExperiment for RNA-Seq in airway smooth muscle cells, by Himes et al PLoS One 2014

	This package provides a RangedSummarizedExperiment object of read counts in genes for an RNA-Seq experiment on four human airway smooth muscle cell lines treated with dexamethasone. Details on the gene model and read counting procedure are provided in the package vignette. The citation for the experiment is: Himes BE, Jiang X, Wagner P, Hu R, Wang Q, Klanderman B, Whitaker RM, Duan Q, Lasky-Su J, Nikolos C, Jester W, Johnson M, Panettieri R Jr, Tantisira KG, Weiss ST, Lu Q. 'RNA-Seq Transcriptome Profiling Identifies CRISPLD2 as a Glucocorticoid Responsive Gene that Modulates Cytokine Function in Airway Smooth Muscle Cells.' PLoS One. 2014 Jun 13;9(6):e99625. PMID: 24926665. GEO: GSE52778.
	"""
	
	bioc = "airway" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/airway_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/airway/airway_1.22.0.tar.gz"]

	version("1.22.0", md5="ffed4ae3349ebeeeabff9f1456b8ba1d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

	# experiment