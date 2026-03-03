# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgst(RPackage):
	"""Leveraging eQTLs to Identify Individual-Level Tissue of Interest
for a Complex Trait

	Genetic predisposition for complex traits is often manifested through multiple tissues of interest at different time points in the development. As an example, the genetic predisposition for obesity could be manifested through inherited variants that control metabolism through regulation of genes expressed in the brain and/or through the control of fat storage in the adipose tissue by dysregulation of genes expressed in adipose tissue. We present a method eGST (eQTL-based genetic subtyper) that integrates tissue-specific eQTLs with GWAS data for a complex trait to probabilistically assign a tissue of interest to the phenotype of each individual in the study. eGST estimates the posterior probability that an individual's phenotype can be assigned to a tissue based on individual-level genotype data of tissue-specific eQTLs and marginal phenotype data in a genome-wide association study (GWAS) cohort. Under a Bayesian framework of mixture model, eGST employs a maximum a posteriori (MAP) expectation-maximization (EM) algorithm to estimate the tissue-specific posterior probability across individuals. Methodology is available from: A Majumdar, C Giambartolomei, N Cai, MK Freund, T Haldar, T Schwarz, J Flint, B Pasaniuc (2019) <doi:10.1101/674226>.
	"""
	
	homepage = "https://github.com/ArunabhaCodes/eGST"
	cran = "eGST" 

	version("1.0.0", md5="37c50481ad18ff50cb826b54812faa12")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
