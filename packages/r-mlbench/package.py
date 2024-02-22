# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlbench(RPackage):
	"""Machine Learning Benchmark Problems.

	A collection of artificial and real-world machine learning benchmark
	problems, including, e.g., several data sets from the UCI repository."""

	cran = "mlbench"

	version("2.1-3.1", md5="052333f1f00cee5907e8621abc047799")

	depends_on("r@2.10:", type=("build", "run"))
