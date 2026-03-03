# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpanet2toolkit(RPackage):
	"""Call 'EPANET' Functions to Simulate Pipe Networks

	Enables simulation of water piping networks using 'EPANET'.
    The package provides functions from the 'EPANET' programmer's toolkit as R
    functions so that basic or customized simulations can be carried out from R.
    The package uses 'EPANET' version 2.2 from Open Water Analytics
    <https://github.com/OpenWaterAnalytics/EPANET/releases/tag/v2.2>.  
	"""
	
	homepage = "https://github.com/bradleyjeck/epanet2toolkit"
	cran = "epanet2toolkit" 

	version("1.0.4", md5="cd19611fea96aaa757a26bbd550f9689")

