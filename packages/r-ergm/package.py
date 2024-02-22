# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErgm(RPackage):
	"""Fit, Simulate and Diagnose Exponential-Family Models for Networks.

	An integrated set of tools to analyze and simulate networks based on
	exponential-family random graph models (ERGMs). 'ergm' is a part of the
	Statnet suite of packages for network analysis. See Hunter, Handcock,
	Butts, Goodreau, and Morris (2008) <doi:10.18637/jss.v024.i03> and
	Krivitsky, Hunter, Morris, and Klumb (2021) <arXiv:2106.04997>."""

	cran = "ergm"

	version("4.6.0", md5="ecbd817b0cd70183e12491d95106f100")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-network@1.18:", type=("build", "run"))
	depends_on("r-robustbase@0.93.7:", type=("build", "run"))
	depends_on("r-coda@0.19.4:", type=("build", "run"))
	depends_on("r-trust@0.1.8:", type=("build", "run"))
	depends_on("r-matrix@1.3.2:", type=("build", "run"))
	depends_on("r-lpsolveapi@5.5.2.0.17.7:", type=("build", "run"))
	depends_on("r-mass@7.3.53.1:", type=("build", "run"))
	depends_on("r-statnet-common@4.9:", type=("build", "run"))
	depends_on("r-rle@0.9.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-memoise@2:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-rdpack@2.4:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("openmpi", type=("build", "link", "run"))

	# The CRAN page list OpenMPI as a dependency but this is not a dependency
	# for using the package. If one wishes to use MPI, simply load an MPI
	# package, along with r-dosnow and r-rmpi when using r-ergm, and set the
	# appropriate options in the R script.
