# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesdesign(RPackage):
	"""Bayesian Single-Arm Design with Survival Endpoints

	The proposed event-driven approach for Bayesian two-stage single-arm phase II trial design is a novel clinical trial design and can be regarded as an extension of the Simon’s two-stage design with the time-to-event endpoint. This design is motivated by cancer clinical trials with immunotherapy and molecularly targeted therapy, in which time-to-event endpoint is often a desired endpoint.
	"""
	
	cran = "BayesDesign" 

	version("0.1.1", md5="e8b51cd32d6c8c50905028e2f6458301")

