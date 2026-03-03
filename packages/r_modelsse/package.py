# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelsse(RPackage):
	"""Modelling Infectious Disease Superspreading from Contact Tracing
Data

	Comprehensive analytical tools are provided to characterize infectious disease superspreading from contact tracing surveillance data. The underlying theoretical frameworks of this toolkit include branching process with transmission heterogeneity (Lloyd-Smith et al. (2005) <doi:10.1038/nature04153>), case cluster size distribution (Nishiura et al. (2012) <doi:10.1016/j.jtbi.2011.10.039>, Blumberg et al. (2014) <doi:10.1371/journal.ppat.1004452>, and Kucharski and Althaus (2015) <doi:10.2807/1560-7917.ES2015.20.25.21167>), and decomposition of reproduction number (Zhao et al. (2022) <doi:10.1371/journal.pcbi.1010281>).
	"""
	
	cran = "modelSSE" 

	version("0.1-3", md5="256cd2ce24ca7539c74c8357f8c5d0c3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-delaporte", type=("build", "run"))
