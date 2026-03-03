# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgip(RPackage):
	"""Data Visualization for IP Addresses and Networks

	A 'ggplot2' extension that enables visualization of IP
    (Internet Protocol) addresses and networks. The address space is
    mapped onto the Cartesian coordinate system using a space-filling
    curve. Offers full support for both IPv4 and IPv6 (Internet Protocol
    versions 4 and 6) address spaces.
	"""
	
	homepage = "https://davidchall.github.io/ggip/"
	cran = "ggip" 

	version("0.3.2", md5="73699309ef85267d18f868e8cb4612f2")

	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ipaddress", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
