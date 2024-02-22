# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwrgsd(RPackage):
	"""Power in a Group Sequential Design

	Tools for the evaluation of interim analysis plans for sequentially
 monitored trials on a survival endpoint; tools to construct efficacy and 
 futility boundaries, for deriving power of a sequential design at a specified
 alternative, template for evaluating the performance of candidate plans at a 
 set of time varying alternatives. See Izmirlian, G. (2014) <doi:10.4310/SII.2014.v7.n1.a4>.
	"""
	
	cran = "PwrGSD" 

	version("2.3.6", md5="5356eb9aeee05fc9f75d085c73c4e426")

	depends_on("r-survival", type=("build", "run"))
