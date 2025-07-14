# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnasense(RPackage):
	"""Analysis of Time-Resolved RNA-Seq Data

	RNA-sense tool compares RNA-seq time curves in two experimental conditions, i.e. wild-type and mutant, and works in three steps. At Step 1, it builds expression profile for each transcript in one condition (i.e. wild-type) and tests if the transcript abundance grows or decays significantly. Dynamic transcripts are then sorted to non-overlapping groups (time profiles) by the time point of switch up or down. At Step 2, RNA-sense outputs the groups of differentially expressed transcripts, which are up- or downregulated in the mutant compared to the wild-type at each time point. At Step 3, Correlations (Fisher's exact test) between the outputs of Step 1 (switch up- and switch down- time profile groups) and the outputs of Step2 (differentially expressed transcript groups) are calculated. The results of the correlation analysis are printed as two-dimensional color plot, with time profiles and differential expression groups at y- and x-axis, respectively, and facilitates the biological interpretation of the data.
	"""
	
	bioc = "RNAsense" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RNAsense_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RNAsense/RNAsense_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="c88e9a3649a8685a158c4ea9f0ce60046b8f090bace686d11a839f90a155bdab")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nbpseq", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
