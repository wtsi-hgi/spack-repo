# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsicsdata(RPackage):
	"""Example of 1D NMR spectra data for ASICS package

	1D NMR example spectra and additional data for use with the ASICS package. Raw 1D Bruker spectral data files were found in the MetaboLights database (https://www.ebi.ac.uk/metabolights/, study MTBLS1).
	"""
	
	bioc = "ASICSdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ASICSdata_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ASICSdata/ASICSdata_1.22.0.tar.gz"]

	version("1.22.0", sha256="c8b8d4df88e867d25a515212e3debde68728f51a3b35f2f1c5fb0c96e411b507")

	depends_on("r@3.5:", type=("build", "run"))

