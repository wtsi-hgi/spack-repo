# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsensusov(RPackage):
	"""Gene expression-based subtype classification for high-grade serous ovarian cancer

	This package implements four major subtype classifiers for high-grade serous (HGS) ovarian cancer as described by Helland et al. (PLoS One, 2011), Bentink et al. (PLoS One, 2012), Verhaak et al. (J Clin Invest, 2013), and Konecny et al. (J Natl Cancer Inst, 2014). In addition, the package implements a consensus classifier, which consolidates and improves on the robustness of the proposed subtype classifiers, thereby providing reliable stratification of patients with HGS ovarian tumors of clearly defined subtype.
	"""
	
	homepage = "http://www.pmgenomics.ca/bhklab/software/consensusOV"
	bioc = "consensusOV" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/consensusOV_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/consensusOV/consensusOV_1.24.0.tar.gz"]

	version("1.24.0", md5="54a03e3c6775a27643ffbf5192967ac2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-genefu", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
