# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimalrerandexpdesigns(RPackage):
	"""Optimal Rerandomization Experimental Designs

	This is a tool to find the optimal rerandomization threshold in non-sequential experiments. We offer three procedures based 
	on assumptions made on the residuals distribution: (1) normality assumed (2) excess kurtosis assumed (3) entire distribution assumed.
	Illustrations are included. Also included is a routine to unbiasedly estimate Frobenius norms of variance-covariance matrices.
	Details of the method can be found in "Optimal Rerandomization via a Criterion that Provides Insurance Against Failed Experiments"
	Adam Kapelner, Abba M. Krieger, Michael Sklar and David Azriel (2020) <arXiv:1905.03337>.
	"""
	
	homepage = "https://github.com/kapelner/OptimalRerandExpDesigns"
	cran = "OptimalRerandExpDesigns" 

	version("1.1", md5="388c4702252dbc772d74f216ca3bc1dd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-momentchi2@0.1.5:", type=("build", "run"))
	depends_on("r-greedyexperimentaldesign@1.3:", type=("build", "run"))
