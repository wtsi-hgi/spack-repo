# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRib(RPackage):
	"""An Implementation of 'Interactive Brokers' API

	Allows interaction with 'Interactive Brokers' 'Trader Workstation'
    <https://interactivebrokers.github.io/tws-api/>.
    Handles the connection over the network and the exchange of messages.
    Data is encoded and decoded between user and wire formats.
    Data structures and functionality closely mirror the official implementations.
	"""
	
	homepage = "https://github.com/lbilli/rib"
	cran = "rib" 

	version("0.19.3", md5="46cc19a5a7e539a46bae115e2c2b773f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-r6@2.4:", type=("build", "run"))
