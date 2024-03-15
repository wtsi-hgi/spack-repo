# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtiger(RPackage):
	"""HMM-Based Model for Genotyping and Cross-Over Identification

	Our method integrates information from all sequenced samples, thus avoiding loss of alleles due to low coverage. Moreover, it increases the statistical power to uncover sequencing or alignment errors <doi:10.1093/plphys/kiad191>. 
	"""
	
	cran = "RTIGER" 

	version("2.1.0", md5="54ffef871739df6b0bcf197cc1441993")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tailrank", type=("build", "run"))
	depends_on("r-juliacall", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
