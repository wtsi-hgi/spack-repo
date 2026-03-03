# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothroctime(RPackage):
	"""Smooth Time-Dependent ROC Curve Estimation

	Computes smooth estimations for the Cumulative/Dynamic and Incident/Dynamic ROC curves, in presence of right censorship, based on the bivariate kernel density estimation of the joint distribution function of the Marker and Time-to-event variables.
	"""
	
	cran = "smoothROCtime" 

	version("0.1.0", md5="b97023bba6e525f651a2915e07a3df54")

	depends_on("r-ks", type=("build", "run"))
