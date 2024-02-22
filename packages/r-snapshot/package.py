# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnapshot(RPackage):
	"""Gadget N-body cosmological simulation code snapshot I/O
utilities

	Functions for reading and writing Gadget N-body snapshots. The Gadget code is popular in astronomy for running N-body / hydrodynamical cosmological and merger simulations. To find out more about Gadget see the main distribution page at www.mpa-garching.mpg.de/gadget/
	"""
	
	cran = "snapshot" 

	version("0.1.2", md5="d73496d3751a47ac4a73badd331ccaae")

	depends_on("r@2.13:", type=("build", "run"))
