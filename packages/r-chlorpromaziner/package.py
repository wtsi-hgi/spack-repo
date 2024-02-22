# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChlorpromaziner(RPackage):
	"""Convert Antipsychotic Doses to Chlorpromazine Equivalents

	As different antipsychotic medications have different potencies,
    the doses of different medications cannot be directly compared. Various
    strategies are used to convert doses into a common reference so that
    comparison is meaningful. Chlorpromazine (CPZ) has historically been used
    as a reference medication into which other antipsychotic doses can be
    converted, as "chlorpromazine-equivalent doses". Using conversion keys
    generated from widely-cited scientific papers, e.g. Gardner et. al 2010
    <doi:10.1176/appi.ajp.2009.09060802> and Leucht et al. 2016
    <doi:10.1093/schbul/sbv167>, antipsychotic doses are converted
    to CPZ (or any specified antipsychotic) equivalents. The use of the package
    is described in the included vignette. Not for clinical use.
	"""
	
	homepage = "https://docs.ropensci.org/chlorpromazineR/"
	cran = "chlorpromazineR" 

	version("0.2.0", md5="7d72a3a391ad684e127571fdd504ab99")

	depends_on("r@3.5:", type=("build", "run"))
