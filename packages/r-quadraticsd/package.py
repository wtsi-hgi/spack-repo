# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuadraticsd(RPackage):
	"""Visualizing the SD using a Quadratic Curve

	Given a dataset, the user is invited to utilize the Empirical Cumulative Distribution Function (ECDF) 
              to guess interactively the mean and the mean deviation. Thereafter,
              using the quadratic curve the user can guess the Root Mean Squared Deviation (RMSD) 
              and visualize the standard deviation (SD). 
              For details, see Sarkar and Rashid (2019)<doi:10.3126/njs.v3i0.25574>, 
              Have You Seen the Standard Deviaton?, Nepalese Journal of Statistics, Vol. 3, 1-10.
	"""
	
	cran = "quadraticSD" 

	version("0.1.0", md5="79afb6799b3906447126d97072f5a36c")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
