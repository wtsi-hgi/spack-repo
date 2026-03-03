# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDpit(RPackage):
	"""Distribution Pitting

	Compares distributions with one another in terms of their fit to each sample in a dataset that contains multiple samples, as described in Joo, Aguinis, and Bradley (in press). Users can examine the fit of seven distributions per sample: pure power law, lognormal, exponential, power law with an exponential cutoff, normal, Poisson, and Weibull. Automation features allow the user to compare all distributions for all samples with a single command line, which creates a separate row containing results for each sample until the entire dataset has been analyzed.
	"""
	
	cran = "Dpit" 

	version("1.0", md5="217d1d119e38b2050e8d4d6fa1153d76")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
