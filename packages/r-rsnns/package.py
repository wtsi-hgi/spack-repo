# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RRsnns(RPackage):
	"""Neural Networks using the Stuttgart Neural Network Simulator (SNNS).

	The Stuttgart Neural Network Simulator (SNNS) is a library containing many
	standard implementations of neural networks. This package wraps the SNNS
	functionality to make it available from within R. Using the RSNNS low-level
	interface, all of the algorithmic functionality and flexibility of SNNS can
	be accessed. Furthermore, the package contains a convenient high-level
	interface, so that the most common neural network topologies and learning
	algorithms integrate seamlessly into R."""

	cran = "RSNNS"

	version("0.4-17", md5="ef3abf228a9823bc553376a63b040b4d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
