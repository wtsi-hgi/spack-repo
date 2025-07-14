# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrebsdata(RPackage):
	"""Data for 'prebs' package

	This package contains data required to run examples in 'prebs' package. The data files include: 1) Small sample bam files for demonstration purposes 2) Probe sequence mappings for Custom CDF (taken from http://brainarray.mbni.med.umich.edu/brainarray/Database/CustomCDF/genomic_curated_CDF.asp) 3) Probe sequence mappings for manufacturer's CDF (manually created using bowtie)
	"""
	
	bioc = "prebsdata"

	version("1.44.0", commit="562e2ca07a522bad317d59761b2652696e2c8355")
	version("1.38.0", commit="893ae5e88f1bef96908b1cefc79932f6c9c933dd")

	depends_on("r@2.14:", type=("build", "run"))

