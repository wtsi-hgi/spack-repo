# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanopy(RPackage):
	"""Accessing Intra-Tumor Heterogeneity and Tracking Longitudinal
and Spatial Clonal Evolutionary History by Next-Generation
Sequencing

	A statistical framework and computational procedure for identifying
  the sub-populations within a tumor, determining the mutation profiles of each 
  subpopulation, and inferring the tumor's phylogenetic history. The input are 
  variant allele frequencies (VAFs) of somatic single nucleotide alterations 
  (SNAs) along with allele-specific coverage ratios between the tumor and matched
  normal sample for somatic copy number alterations (CNAs). These quantities can
  be directly taken from the output of existing software. Canopy provides a 
  general mathematical framework for pooling data across samples and sites to 
  infer the underlying parameters. For SNAs that fall within CNA regions, Canopy
  infers their temporal ordering and resolves their phase.  When there are 
  multiple evolutionary configurations consistent with the data, Canopy outputs 
  all configurations along with their confidence assessment.
	"""
	
	homepage = "https://github.com/yuchaojiang/Canopy"
	cran = "Canopy" 

	version("1.3.0", md5="744849b76bb5560ef3e0ed47ae110f48")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
