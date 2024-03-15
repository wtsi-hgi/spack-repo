# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiasedurn(RPackage):
	"""Biased Urn Model Distributions.

	Statistical models of biased sampling in the form of univariate and
	multivariate noncentral hypergeometric distributions, including Wallenius'
	noncentral hypergeometric distribution and Fisher's noncentral
	hypergeometric distribution (also called extended hypergeometric
	distribution). See vignette("UrnTheory") for explanation of these
	distributions."""

	cran = "BiasedUrn"

	version("2.0.11", md5="435d436db9c8359cf99234f9468bfc78")

