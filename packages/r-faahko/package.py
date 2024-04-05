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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/faahKO_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/faahKO/faahKO_1.42.0.tar.gz"]

	version("1.42.0", md5="3525f525973323d33955a68ca38b5cd7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xcms@3.4:", type=("build", "run"))

