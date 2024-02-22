# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLegit(RPackage):
	"""Latent Environmental & Genetic InTeraction (LEGIT) Model

	Constructs genotype x environment interaction (GxE) models where
    G is a weighted sum of genetic variants (genetic score) and E is a weighted
    sum of environments (environmental score) using the alternating optimization algorithm 
    by Jolicoeur-Martineau et al. (2017) <arXiv:1703.08111>. This approach has greatly 
    enhanced predictive power over traditional GxE models which include only a single 
    genetic variant and a single environmental exposure. Although this approach was 
    originally made for GxE modelling, it is flexible and does not require the use of 
    genetic and environmental variables. It can also handle more than 2 latent variables 
    (rather than just G and E) and 3-way interactions or more. The LEGIT model produces 
    highly interpretable results and is very parameter-efficient thus it can even be 
    used with small sample sizes (n < 250). Tools to determine the type of interaction
    (vantage sensitivity, diathesis-stress or differential susceptibility), with any 
    number of genetic variants or environments, are available <arXiv:1712.04058>. The 
    software can now produce mixed-effects LEGIT models through the lme4 package.
	"""
	
	cran = "LEGIT" 

	version("1.4.1", md5="0f1a5696e775de87d6ed41276f91fdec")

	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
