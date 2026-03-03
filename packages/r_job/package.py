# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJob(RPackage):
	"""Run Code as an RStudio Job - Free Your Console

	Call job::job({<code here>}) to run R code as an RStudio job and keep your console free in the meantime. This allows for a productive workflow while testing (multiple) long-running chunks of code. It can also be used to organize results using the RStudio Jobs GUI or to test code in a clean environment. Two RStudio Addins can be used to run selected code as a job.
	"""
	
	cran = "job" 

	version("0.3.0", md5="3d361f30661adc641e80391e3ee8d96a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rstudioapi@0.13:", type=("build", "run"))
	depends_on("r-digest@0.6.27:", type=("build", "run"))
