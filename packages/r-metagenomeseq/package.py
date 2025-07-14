# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetagenomeseq(RPackage):
	"""Statistical analysis for sparse high-throughput sequencing

	metagenomeSeq is designed to determine features (be it Operational Taxanomic Unit (OTU), species, etc.) that are differentially abundant between two or more groups of multiple samples. metagenomeSeq is designed to address the effects of both normalization and under-sampling of microbial communities on disease association detection and the testing of feature correlations.
	"""
	
	homepage = "https://github.com/nosson/metagenomeSeq/"
	bioc = "metagenomeSeq"

	version("1.50.0", commit="0acf3eb56ad231cc8d672d1b7fc80ca82457b6ea")
	version("1.43.0", sha256="8b685245818596b23fa3ca508cb5c2c1e635d494eec79017f424bb95f9c429d4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-wrench", type=("build", "run"))
