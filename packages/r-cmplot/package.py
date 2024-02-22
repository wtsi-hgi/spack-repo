# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmplot(RPackage):
	"""Circle Manhattan Plot

	Manhattan plot, a type of scatter plot, was widely used to display the association results. However, it is usually time-consuming and laborious for a non-specialist user to write scripts and adjust parameters of an elaborate plot. Moreover, the ever-growing traits measured have necessitated the integration of results from different Genome-wide association study researches. Circle Manhattan Plot is the first open R package that can lay out. Genome-wide association study P-value results in both traditional rectangular patterns, QQ-plot and novel circular ones. United in only one bull's eye style plot, association results from multiple traits can be compared interactively, thereby to reveal both similarities and differences between signals. Additional functions include: highlight signals, a group of SNPs, chromosome visualization and candidate genes around SNPs.
	"""
	
	homepage = "https://github.com/YinLiLin/CMplot"
	cran = "CMplot" 

	version("4.5.1", md5="f32790ba773b4aca62c301d2d7045d3c")

	depends_on("r@2.10:", type=("build", "run"))
