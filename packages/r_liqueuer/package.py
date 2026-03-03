# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiqueuer(RPackage):
	"""Implements Queue, PriorityQueue and Stack Classes

	Provides three classes: Queue, PriorityQueue and Stack. Queue is just a
    "plain vanilla" FIFO queue; PriorityQueue orders items according to priority. Stack implements LIFO.
	"""
	
	homepage = "https://github.com/DataWookie/liqueueR"
	cran = "liqueueR" 

	version("0.0.1", md5="9cab2d2ce8002e6ec012c37f5bca2ec8")

	depends_on("r-itertools", type=("build", "run"))
