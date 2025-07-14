# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsgbsr(RPackage):
	"""msgbsR: methylation sensitive genotyping by sequencing (MS-GBS) R functions

	Pipeline for the anaysis of a MS-GBS experiment.
	"""
	
	bioc = "msgbsR"

	version("1.32.0", commit="b76e4e288d41f495c5915878ade643b559136449")
	version("1.26.0", commit="0b34e7d8c44824ac7fa1884c010685831ffe1cde")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-easyrnaseq", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-ggbio", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
