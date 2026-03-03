# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgseqplot(RPackage):
	"""Render Sequence Plots using 'ggplot2'

	A set of wrapper functions that mainly re-produces most of the 
  sequence plots rendered with TraMineR::seqplot(). Whereas 'TraMineR' uses base 
  R to produce the plots this library draws on 'ggplot2'. 
  The plots are produced on the basis of a sequence object defined  
  with TraMineR::seqdef(). The package automates the reshaping and plotting 
  of sequence data. Resulting plots are of class 'ggplot', i.e. components 
  can be added and tweaked using '+' and regular 'ggplot2' functions. 
	"""
	
	homepage = "https://maraab23.github.io/ggseqplot/"
	cran = "ggseqplot" 

	version("0.8.3", md5="a0d2a904189c27d885f1cebb113fc93c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-traminer@2.2.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-ggh4x", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
