# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyntenyplotter(RPackage):
	"""Genome Synteny Visualization

	Draw syntenic relationships between genome assemblies.
    There are 3 functions which take a tab delimited file containing alignment data for 
    syntenic blocks between genomes to produce either a linear alignment plot, 
    an evolution highway style plot, or a painted ideogram representing syntenic relationships.
    There is also a function to convert alignment data in the DESCHRAMBLER/inferCAR format
    to the required data structure.
	"""
	
	cran = "syntenyPlotteR" 

	version("1.0.0", md5="14afb82af3dc2c810fc8146d955a5899")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
