# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatstatRandom(RPackage):
	"""Random Generation Functionality for the 'spatstat' Family.

	Functionality for random generation of spatial data in the 'spatstat'
	family of packages. Generates random spatial patterns of points according
	to many simple rules (complete spatial randomness, Poisson, binomial,
	random grid, systematic, cell), randomised alteration of patterns
	(thinning, random shift, jittering), simulated realisations of random point
	processes (simple sequential inhibition, Matern inhibition models, Matern
	cluster process, Neyman-Scott cluster processes, log-Gaussian Cox
	processes, product shot noise cluster processes) and simulation of Gibbs
	point processes (Metropolis-Hastings birth-death-shift algorithm,
	alternating Gibbs sampler). Also generates random spatial patterns of line
	segments, random tessellations, and random images (random noise, random
	mosaics). Excludes random generation on a linear network, which is covered
	by the separate package 'spatstat.linnet'."""

	cran = "spatstat.random"

	version("3.2-2", md5="951293b3cd32fdaed6011187826f1472")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat-data@3:", type=("build", "run"))
	depends_on("r-spatstat-geom@3.2.1:", type=("build", "run"))
	depends_on("r-spatstat-utils@3.0.2:", type=("build", "run"))
