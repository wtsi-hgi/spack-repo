# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosaics(RPackage):
	"""MOSAiCS (MOdel-based one and two Sample Analysis and Inference for ChIP-Seq)

	This package provides functions for fitting MOSAiCS and MOSAiCS-HMM, a statistical framework to analyze one-sample or two-sample ChIP-seq data of transcription factor binding and histone modification.
	"""
	
	homepage = "http://groups.google.com/group/mosaics_user_group"
	bioc = "mosaics" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mosaics_2.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mosaics/mosaics_2.40.0.tar.gz"]

	version("2.40.0", sha256="059be9cc10690f42bd5031aa17f05a9db0f6d0f1163e6eaf76b63979787225ea")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("perl", type=("build", "link", "run"))
