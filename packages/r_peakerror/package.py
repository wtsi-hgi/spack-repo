# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeakerror(RPackage):
	"""Compute the Label Error of Peak Calls

	Chromatin immunoprecipitation DNA sequencing results in genomic
    tracks that show enriched regions or peaks where proteins are bound.
    This package implements fast C code that computes the true and false
    positives with respect to a database of annotated region labels.
	"""
	
	cran = "PeakError" 

	version("2023.9.4", md5="6d600e30b1c0b9fc52d75f31f04356ef")

