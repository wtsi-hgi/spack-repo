# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinet(RPackage):
	"""Mutual Information NETworks

	This package implements various algorithms for inferring mutual information networks from data.
	"""
	
	homepage = "http://minet.meyerp.com"
	bioc = "minet"

	version("3.66.0", commit="902efa9808a437c93dc642f9278c2038df52618b")
	version("3.60.0", commit="3cf4b451b6d96befa967e91eade33d61a37b003e")

	depends_on("r-infotheo", type=("build", "run"))
