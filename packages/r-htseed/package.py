# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtseed(RPackage):
	"""Fitting of Hydrotime Model for Seed Germination Time Course

	The seed germination process starts with water uptake by the seed and ends with the protrusion of radicle and plumule under varying temperatures and soil water potential. Hydrotime is a way to describe the relationship between water potential and seed germination rates at germination percentages. One important quantity before applying hydrotime modeling of germination percentages is to consider the proportion of viable seeds that could germinate under saturated conditions. This package can be used to apply correction factors at various water potentials before estimating parameters like stress tolerance, and uniformity of the hydrotime model. Three different distributions namely, Gaussian, Logistic, and Extreme value distributions have been considered to fit the model to the seed germination time course. Details can be found in Bradford (2002) <https://www.jstor.org/stable/4046371>, and Bradford and Still(2004) <https://www.jstor.org/stable/23433495>. 
	"""
	
	cran = "HTSeed" 

	version("0.1.0", md5="d28f7cfa58f348a34ae7473f540bd4b7")

	depends_on("r-dplyr", type=("build", "run"))
