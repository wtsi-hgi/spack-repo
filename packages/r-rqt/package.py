# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRqt(RPackage):
	"""rqt: utilities for gene-level meta-analysis

	Despite the recent advances of modern GWAS methods, it still remains an important problem of addressing calculation an effect size and corresponding p-value for the whole gene rather than for single variant. The R- package rqt offers gene-level GWAS meta-analysis. For more information, see: "Gene-set association tests for next-generation sequencing data" by Lee et al (2016), Bioinformatics, 32(17), i611-i619, <doi:10.1093/bioinformatics/btw429>.
	"""
	
	homepage = "https://github.com/izhbannikov/rqt"
	bioc = "rqt" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rqt_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rqt/rqt_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="5071d7c52b74741377dc307cf3e498786af90baedcc140140fbd0386cce5db0b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ropls", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-metap", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
