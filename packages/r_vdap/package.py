# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVdap(RPackage):
	"""Peptide Array Analysis Tools

	Analyze Peptide Array Data and characterize peptide
    sequence space. Allows for high level visualization of global signal, Quality control based
    on replicate correlation and/or relative Kd, calculation of peptide Length/Charge/Kd parameters,
    Hits selection based on RFU Signal, and amino acid composition/basic motif recognition with RFU
    signal weighting. Basic signal trends can be used to generate peptides that follow the observed
    compositional trends.
	"""
	
	cran = "VDAP" 

	version("2.0.0", md5="9998953f522d52b7c21724d55d700601")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
