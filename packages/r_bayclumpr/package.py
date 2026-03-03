# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayclumpr(RPackage):
	"""Bayesian Analysis of Clumped Isotope Datasets

	Simulating synthetic clumped isotope dataset, fitting
    linear regression models under Bayesian and non-Bayesian frameworks,
    and generating temperature reconstructions for the same two approaches.
    Please note that models implemented in this package are described
    in Roman-Palacios et al. (2021) <doi:10.1002/essoar.10507995.1>.
	"""
	
	homepage = "https://bayclump.tripatilab.epss.ucla.edu/"
	cran = "bayclumpr" 

	version("0.1.0", md5="9a7932a84e2ab256ac3023587767fe9a")

	depends_on("r-loo", type=("build", "run"))
	depends_on("r-deming", type=("build", "run"))
	depends_on("r-isoplotr", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
