# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetalonda(RPackage):
	"""Metagenomics Longitudinal Differential Abundance Method

	Identify time intervals of differentially abundant metagenomic features in longitudinal studies (Metwally AA, et al., Microbiome, 2018 <doi:10.1186/s40168-018-0402-y>).
	"""
	
	homepage = "https://github.com/aametwally/MetaLonDA"
	cran = "MetaLonDA" 

	version("1.1.8", md5="e85311a09811813c77fad133f1ffc603")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gss", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-metagenomeseq", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
