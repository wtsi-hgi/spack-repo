# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDqtgSeq(RPackage):
	"""A BSA Software for Detecting All Types of QTLs in BC, DH, RIL
and F2

	The new (dQTG.seq1 and dQTG.seq2) and existing (SmoothLOD, G', deltaSNP and ED) bulked segregant analysis methods are used to identify various types of quantitative trait loci for complex traits via extreme phenotype individuals in bi-parental segregation populations (F2, backcross, doubled haploid and recombinant inbred line). The numbers of marker alleles in extreme low and high pools are used in existing methods to identify trait-related genes, while the numbers of marker alleles and genotypes in extreme low and high pools are used in the new methods to construct a new statistic Gw for identifying trait-related genes. dQTG-seq2 is feasible to identify extremely over-dominant and small-effect genes in F2. Li P, Li G, Zhang YW, Zuo JF, Liu JY, Zhang YM (2022, <doi: 10.1016/j.xplc.2022.100319>).      
	"""
	
	cran = "dQTG.seq" 

	version("1.0.2", md5="850cdf61b7ef075b3f09d062ded25491")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
