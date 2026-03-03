# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSusy(RPackage):
	"""Surrogate Synchrony

	Computes synchrony as windowed cross-correlation based on two-dimensional time series in a text file you can upload. 'SUSY' works as described in Tschacher & Meier (2020) <doi:10.1080/10503307.2019.1612114>.
	"""
	
	homepage = "https://wtschacher.github.io/SUSY/"
	cran = "SUSY" 

	version("0.1.0", md5="f31dbd91b4f363feffd95995c63d1bd6")

