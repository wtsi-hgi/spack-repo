# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrcs(RPackage):
	"""Omnidirectional R Code Snippets

	I tend to repeat the same code chunks over and over again. At
    first, this was fine for me and I paid little attention to such redundancies.
    A little later, when I got tired of manually replacing Linux filepaths with
    the referring Windows versions, and vice versa, I started to stuff some very
    frequently used work-steps into functions and, even later, into a proper R
    package. And that's what this package is - a hodgepodge of various R functions
    meant to simplify (my) everyday-life coding work without, at the same time,
    being devoted to a particular scope of application.
	"""
	
	homepage = "https://github.com/fdetsch/Orcs"
	cran = "Orcs" 

	version("1.2.3", md5="13eb18d8ab21598fc38f92f8cffc271a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("7zip", type=("build", "link", "run"))
