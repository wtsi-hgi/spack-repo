# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatasetsuni(RPackage):
	"""A Collection of Univariate Data Sets

	A collection of widely used univariate data sets of various applied domains on applications of distribution theory. The functions allow researchers and practitioners to quickly, easily, and efficiently access and use these data sets. The data are related to different applied domains and as follows: Bio-medical, survival analysis, medicine, reliability analysis, hydrology, actuarial science, operational research, meteorology, extreme values, quality control, engineering, finance, sports and economics. The total 100 data sets are documented along with associated references for further details and uses.     
	"""
	
	cran = "DataSetsUni" 

	version("0.1", md5="903384eb1b95b2763b7d683b3d993eb8")

	depends_on("r@3.5:", type=("build", "run"))
