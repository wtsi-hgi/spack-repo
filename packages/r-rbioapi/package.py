# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbioapi(RPackage):
	"""User-Friendly R Interface to Biologic Web Services' API

	Currently fully supports Enrichr, JASPAR, miEAA, PANTHER,
    Reactome, STRING, and UniProt! The goal of rbioapi is to provide a
    user-friendly and consistent interface to biological databases and
    services. In a way that insulates the user from the technicalities of
    using web services API and creates a unified and easy-to-use interface
    to biological and medical web services. This is an ongoing project; New
    databases and services will be added periodically. Feel free to
    suggest any databases or services you often use.
	"""
	
	homepage = "https://rbioapi.moosa-r.com"
	cran = "rbioapi" 

	version("0.8.1", md5="eec2583a4242af6e318612e49528d6fb")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
