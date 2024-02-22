# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMycobacrvr(RPackage):
	"""Integrative Immunoinformatics for Mycobacterial Diseases in R
Platform

	The mycobacrvR package contains utilities to provide detailed information for B cell and T cell epitopes for predicted adhesins from various servers such as ABCpred, Bcepred, Bimas, Propred, NetMHC and IEDB. Please refer the URL below to download data files (data_mycobacrvR.zip) used in functions of this package.
	"""
	
	homepage = "https://mycobacteriarv.igib.res.in/download.html"
	cran = "mycobacrvR" 

	version("1.1", md5="54c6ada7e00db4144816a2a70861a99c")

	depends_on("r@2.15:", type=("build", "run"))
