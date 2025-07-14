# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinesath1probe(RPackage):
	"""Probe sequence data for microarrays of type tinesath1

	This package was automatically created by package matchprobes version 1.4.0. The probe sequence data was obtained from http://www.affymetrix.com.
	"""
	
	bioc = "tinesath1probe"

	version("1.46.0", commit="cac3c98c93d03872ef288d0a24634c4096765be6")
	version("1.40.0", commit="a6bf28861fc8795d1e6f8a57e440769331cb669d")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.9:", type=("build", "run"))

