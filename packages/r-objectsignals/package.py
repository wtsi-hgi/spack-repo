# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObjectsignals(RPackage):
	"""Observer Pattern for S4

	A mutable Signal object can report changes to its state,
    clients could register functions so that they are called whenever
    the signal is emitted. The signal could be emitted, disconnected,
    blocked, unblocked, and buffered.
	"""
	
	cran = "objectSignals" 

	version("0.10.3", md5="6b76acd9915ae4bd1e9b84d972810360")

	depends_on("r@2.12:", type=("build", "run"))
