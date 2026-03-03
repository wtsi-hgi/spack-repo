# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsciichartr(RPackage):
	"""Lightweight ASCII Line Graphs

	Create ASCII line graphs of a time series directly on
    your terminal in an easy way. There are some configurations you
    can add to make the plot the way you like. This project was
    inspired by the original 'asciichart' package by Igor Kroitor.
	"""
	
	cran = "asciichartr" 

	version("0.1.0", md5="b7deb0bb4e3ab5ba5ec71b451970f819")

