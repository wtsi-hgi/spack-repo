# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMullerplot(RPackage):
	"""Generates Muller Plot from Population/Abundance/Frequency
Dynamics Data

	Generates Muller plot from parental/genealogy/phylogeny information and population/abundance/frequency dynamics data.
    Muller plots are plots which combine information about succession of different OTUs (genotypes, phenotypes, species, ...) and information about dynamics of their abundances (populations or frequencies) over time. They are powerful and fascinating tools to visualize evolutionary dynamics. They may be employed also in study of diversity and its dynamics, i.e. how diversity emerges and how changes over time. They are called Muller plots in honor of Hermann Joseph Muller which used them to explain his idea of Muller's ratchet (Muller, 1932, American Naturalist).
    A big difference between Muller plots and normal box plots of abundances is that a Muller plot depicts not only the relative abundances but also succession of OTUs based on their genealogy/phylogeny/parental relation. In a Muller plot, horizontal axis is time/generations and vertical axis represents relative abundances of OTUs at the corresponding times/generations. Different OTUs are usually shown with polygons with different colors and each OTU originates somewhere in the middle of its parent area in order to illustrate their succession in evolutionary process.
    To generate a Muller plot one needs the genealogy/phylogeny/parental relation of OTUs and their abundances over time.
    MullerPlot package has the tools to generate Muller plots which clearly depict the origin of successors of OTUs.
	"""
	
	cran = "MullerPlot" 

	version("0.1.3", md5="ac4ccce666b9fd2357c442e66df779a6")

	depends_on("r-rcolorbrewer", type=("build", "run"))
