# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepsavims(RPackage):
	"""PepSAVI-MS Data Analysis

	An implementation of the data processing and data analysis portion
    of a pipeline named the PepSAVI-MS which is currently under development by
    the Hicks laboratory at the University of North Carolina.  The statistical
    analysis package presented herein provides a collection of software tools
    used to facilitate the prioritization of putative bioactive peptides from a
    complex biological matrix.  Tools are provided to deconvolute mass
    spectrometry features into a single representation for each peptide charge
    state, filter compounds to include only those possibly contributing to the
    observed bioactivity, and prioritize these remaining compounds for those
    most likely contributing to each bioactivity data set.
	"""
	
	homepage = "https://github.com/dpritchLibre/PepSAVIms"
	cran = "PepSAVIms" 

	version("0.9.1", md5="6deb2551762f895d4c7acc5127465cb7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
