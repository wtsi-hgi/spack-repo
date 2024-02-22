# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsplots(RPackage):
	"""Stock Status Plots (SSPs)

	Pauly et al. (2008) <http://legacy.seaaroundus.s3.amazonaws.com/doc/Researcher+Publications/dpauly/PDF/2008/Books%26Chapters/FisheriesInLargeMarineEcosystems.pdf> created (and coined the name) 'Stock Status Plots' for a UNEP compendium on Large Marine Ecosystems (LMEs, Sherman and Hempel 2008 <https://agris.fao.org/agris-search/search.do?recordID=XF2015036057>). Stock status plots are bivariate graphs summarizing the status (e.g., developing, fully exploited, overexploited, etc.), through time, of the multispecies fisheries of a fished area or ecosystem. This package contains two functions to generate stock status plots viz., SSplots_pauly() (as per the criteria proposed by Pauly et al.,2008) and SSplots_kleisner() (as per the criteria proposed by Kleisner and Pauly (2011) <http://www.ecomarres.com/downloads/regional.pdf> and Kleisner et al. (2013) <doi:10.1111/j.1467-2979.2012.00469.x>).
	"""
	
	cran = "SSplots" 

	version("0.1.1", md5="89a1e9b0a278b9b1efbedb55853efe82")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
