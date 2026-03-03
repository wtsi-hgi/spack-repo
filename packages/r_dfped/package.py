# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfped(RPackage):
	"""Extrapolation and Bridging of Adult Information in Early Phase
Dose-Finding Paediatrics Studies

	A unified method for designing and analysing dose-finding trials in paediatrics, while bridging information from adults, is proposed in the 'dfped' package. The dose range can be calculated under three extrapolation methods: linear, allometry and maturation adjustment, using pharmacokinetic (PK) data. To do this, it is assumed that target exposures are the same in both populations. The working model and prior distribution parameters of the dose-toxicity and dose-efficacy relationships can be obtained using early phase adult toxicity and efficacy data at several dose levels through 'dfped' package. Priors are used into the dose finding process through a Bayesian model selection or adaptive priors, to facilitate adjusting the amount of prior information to differences between adults and children. This calibrates the model to adjust for misspecification if the adult and paediatric data are very different. User can use his/her own Bayesian model written in Stan code through the 'dfped' package. A template of this model is proposed in the examples of the corresponding R functions in the package. Finally, in this package you can find a simulation function for one trial or for more than one trial. These methods are proposed by Petit et al, (2016) <doi:10.1177/0962280216671348>.
	"""
	
	homepage = "http://github.com/artemis-toumazi/dfped"
	cran = "dfped" 

	version("1.1", md5="39f9295796bcc9b57b366dd397b923b6")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rstan@2.8.1:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
