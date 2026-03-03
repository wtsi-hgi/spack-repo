# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHaplin(RPackage):
	"""Analyzing Case-Parent Triad and/or Case-Control Data with SNP
Haplotypes

	Performs genetic association analyses of case-parent triad (trio) data with multiple markers. It can also incorporate complete or incomplete control triads, for instance independent control children. Estimation is based on haplotypes, for instance SNP haplotypes, even though phase is not known from the genetic data. 'Haplin' estimates relative risk (RR + conf.int.) and p-value associated with each haplotype. It uses maximum likelihood estimation to make optimal use of data from triads with missing genotypic data, for instance if some SNPs has not been typed for some individuals. 'Haplin' also allows estimation of effects of maternal haplotypes and parent-of-origin effects, particularly appropriate in perinatal epidemiology. 'Haplin' allows special models, like X-inactivation, to be fitted on the X-chromosome. A GxE analysis allows testing interactions between environment and all estimated genetic effects. The models were originally described in "Gjessing HK and Lie RT. Case-parent triads: Estimating single- and double-dose effects of fetal and maternal disease gene haplotypes. Annals of Human Genetics (2006) 70, pp. 382-396".
	"""
	
	homepage = "https://haplin.bitbucket.io"
	cran = "Haplin" 

	version("7.3.1", md5="a1181a57e8fd2c617781e46b9821f7c5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
