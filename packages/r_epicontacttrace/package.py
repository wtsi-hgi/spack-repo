# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpicontacttrace(RPackage):
	"""Epidemiological Tool for Contact Tracing

	Routines for epidemiological contact tracing
    and visualisation of network of contacts.
	"""
	
	homepage = "https://github.com/stewid/EpiContactTrace"
	cran = "EpiContactTrace" 

	version("0.17.0", md5="c4cc98f65abe0a109c908d1d48b51064")

	depends_on("r@3.0.2:", type=("build", "run"))
