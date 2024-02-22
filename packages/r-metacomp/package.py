# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetacomp(RPackage):
	"""EDGE Taxonomy Assignments Visualization

	Implements routines for metagenome sample taxonomy assignments collection, 
    aggregation, and visualization. Accepts the EDGE-formatted output from GOTTCHA/GOTTCHA2, 
    BWA, Kraken, MetaPhlAn, DIAMOND, and Pangia. Produces SVG and PDF heatmap-like plots 
    comparing taxa abundances across projects. 
	"""
	
	homepage = "https://github.com/seninp-bioinfo/MetaComp"
	cran = "MetaComp" 

	version("1.1.2", md5="d2973b89300ce80997a28ef4fc2efab4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
