# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFaahko(RPackage):
	"""Saghatelian et al. (2004) FAAH knockout LC/MS data

	Positive ionization mode data in NetCDF file format. Centroided subset from 200-600 m/z and 2500-4500 seconds. Data originally reported in "Assignment of Endogenous Substrates to Enzymes by Global Metabolite Profiling" Biochemistry; 2004; 43(45). Also includes detected peaks in an xcmsSet.
	"""
	
	homepage = "http://dx.doi.org/10.1021/bi0480335"
	bioc = "faahKO"

	version("1.48.1", commit="15e744f7078123765cc577317e027c46fb0dc6bc")
	version("1.42.0", commit="8b35271dab083b47415df0c874eec3bcc610fc8b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xcms@3.4:", type=("build", "run"))

