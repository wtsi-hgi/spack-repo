# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRess(RPackage):
	"""Integrates R and Essentia

	Contains three functions that query AuriQ Systems' Essentia Database and return the results in R. 'essQuery' takes a single Essentia command and captures the output in R, where you can save the output to a dataframe or stream it directly into additional analysis. 'read.essentia' takes an Essentia script and captures the output csv data into R, where you can save the output to a dataframe or stream it directly into additional analysis. 'capture.essentia' takes a file containing any number of Essentia commands and captures the output of the specified statements into R dataframes. Essentia can be downloaded for free at http://www.auriq.com/documentation/source/install/index.html.
	"""
	
	cran = "RESS" 

	version("1.3", md5="acd2cb93f5d549639143f22a7d6323f1")

