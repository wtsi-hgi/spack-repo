# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrecisetadhub(RPackage):
	"""Pre-trained random forest models obtained using preciseTAD

	An experimentdata package to supplement the preciseTAD package containing pre-trained models and the variable importances of each genomic annotation used to build the model parsed into list objects and available in ExperimentHub. In total, preciseTADhub provides access to n=84 random forest classification models optimized to predict TAD/chromatin loop boundary regions and stored as .RDS files. The value, n, comes from the fact that we considered l=2 cell lines {GM12878, K562}, g=2 ground truth boundaries {Arrowhead, Peakachu}, and c=21 autosomal chromosomes {CHR1, CHR2, ..., CHR22} (omitting CHR9). Furthermore, each object is itself a two-item list containing: (1) the model object, and (2) the variable importances for CTCF, RAD21, SMC3, and ZNF143 used to predict boundary regions. Each model is trained via a "holdout" strategy, in which data from chromosomes {CHR1, CHR2, ..., CHRi-1, CHRi+1, ..., CHR22} were used to build the model and the ith chromosome was reserved for testing. See https://doi.org/10.1101/2020.09.03.282186 for more detail on the model building strategy.
	"""
	
	homepage = "https://github.com/dozmorovlab/preciseTADhub"
	bioc = "preciseTADhub" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/preciseTADhub_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/preciseTADhub/preciseTADhub_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="2d8ae69f264e8502492a423bfb644135f855f408336fdb89f572989dcf6ad300")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

