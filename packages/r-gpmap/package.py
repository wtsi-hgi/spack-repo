# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpmap(RPackage):
	"""Analysing and Plotting Genotype-Phenotype Maps

	Tools for studying genotype-phenotype maps for bi-allelic loci underlying quantitative phenotypes. The 0.1 version is released in connection with the publication of Gjuvsland et al (2013) and implements basic line plots and the monotonicity measures for GP maps presented in the paper. Reference: Gjuvsland AB, Wang Y, Plahte E and Omholt SW (2013) Monotonicity is a key feature of genotype-phenotype maps. Frontier in Genetics 4:216 <doi:10.3389/fgene.2013.00216>.
	"""
	
	cran = "gpmap" 

	version("0.1.2", md5="19589ad886a4df561e4d37dc6f8c375c")

	depends_on("r-isotone", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
