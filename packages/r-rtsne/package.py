# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtsne(RPackage):
	"""T-Distributed Stochastic Neighbor Embedding using a Barnes-Hut
	Implementation.

	An R wrapper around the fast T-distributed Stochastic Neighbor Embedding
	implementation."""

	cran = "Rtsne"
	version("0.16", sha256="52a05adc826c28212e97d11c54eba3fec45d14eb52039c0f47f62a8e338ffbd5")
	version("0.15", sha256="56376e4f0a382fad3d3d40e2cb0562224be5265b827622bcd235e8fc63df276c")
	version("0.13", sha256="1c3bffe3bd11733ee4fe01749c293669daafda1af2ec74f9158f6080625b999d")
	version("0.11", sha256="1e2e7368f3de870b9270f70b207ba9e8feea67f9b061cb6abb2fec785fb7247e")
	version("0.10", sha256="c54371f4a935520e7e7ab938ef8f5f7f9ad2a829123b9513ae715c07de034790")
	version("0.17", md5="06863d3c06a170d03d3600d78a80052a")

	depends_on("r-rcpp", type=("build", "run"))
