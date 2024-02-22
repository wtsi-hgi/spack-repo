# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDpcp(RPackage):
	"""Automated Analysis of Multiplex Digital PCR Data

	The automated clustering and quantification of the digital PCR
            data is based on the combination of 'DBSCAN' (Hahsler et al. (2019)
            <doi:10.18637/jss.v091.i01>) and 'c-means' (Bezdek et al. (1981) 
            <doi:10.1007/978-1-4757-0450-1>) algorithms.
            The analysis is independent of multiplexing geometry, dPCR system, 
            and input amount.
            The details about input data and parameters are available in the
            vignette. 
	"""
	
	homepage = "https://github.com/alfodefalco/dPCP"
	cran = "dPCP" 

	version("2.0.1", md5="b6113fb66c41bdcaa9163aa426b206ac")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-exactci", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
