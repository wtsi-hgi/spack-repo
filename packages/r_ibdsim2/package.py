# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbdsim2(RPackage):
	"""Simulation of Chromosomal Regions Shared by Family Members

	Simulation of segments shared identical-by-descent (IBD) by
    pedigree members. Using sex specific recombination rates along the
    human genome (Halldorsson et al. (2019)
    <doi:10.1126/science.aau1043>), phased chromosomes are simulated for
    all pedigree members. Applications include calculation of realised
    relatedness coefficients and IBD segment distributions. 'ibdsim2' is
    part of the 'ped suite' collection of packages for pedigree analysis.
    A detailed presentation of the 'ped suite', including a separate
    chapter on 'ibdsim2', is available in the book 'Pedigree analysis in
    R' (Vigeland, 2021, ISBN:9780128244302). A 'shiny' app for visualising
    and comparing IBD distributions is available at
    <https://magnusdv.shinyapps.io/ibdsim2-shiny/>.
	"""
	
	homepage = "https://github.com/magnusdv/ibdsim2"
	cran = "ibdsim2" 

	version("2.0.0", md5="0258fdee32f617da2ba4ad2c2bcb3a7d", url="https://cran.r-project.org/src/contrib/ibdsim2_2.0.0.tar.gz")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-pedtools@2.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-ribd@1.5:", type=("build", "run"))
