# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMutsignatures(RPackage):
	"""Decipher Mutational Signatures from Somatic Mutational Catalogs

	Cancer cells accumulate DNA mutations as result of DNA damage and DNA repair processes. This computational framework is aimed at deciphering DNA mutational signatures operating in cancer. The framework includes modules that support raw data import and processing, mutational signature extraction, and results interpretation and visualization. The framework accepts widely used file formats storing information about DNA variants, such as Variant Call Format files. The framework performs Non-Negative Matrix Factorization to extract mutational signatures explaining the observed set of DNA mutations. Bootstrapping is performed as part of the analysis. The framework supports parallelization and is optimized for use on multi-core systems. The software was described by Fantini D et al (2020) <doi:10.1038/s41598-020-75062-0> and is based on a custom R-based implementation of the original MATLAB WTSI framework by Alexandrov LB et al (2013) <doi:10.1016/j.celrep.2012.12.008>.   
	"""
	
	homepage = "https://www.data-pulse.com/dev_site/mutsignatures/"
	cran = "mutSignatures" 

	version("2.1.1", md5="79476a953d9f3014e573bf76fda3edb4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
