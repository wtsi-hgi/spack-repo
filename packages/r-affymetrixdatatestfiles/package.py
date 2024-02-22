# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffymetrixdatatestfiles(RPackage):
	"""Affymetrix Data Files (CEL, CDF, CHP, EXP, PGF, PSI) for Testing

	This package contains annotation data files and sample data files of Affymetrix file formats.  The files originate from the Affymetrix' Fusion SDK distribution and other official sources.
	"""
	
	bioc = "AffymetrixDataTestFiles" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/AffymetrixDataTestFiles_0.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/AffymetrixDataTestFiles/AffymetrixDataTestFiles_0.40.0.tar.gz"]

	version("0.40.0", md5="57ecb8e4d3f0d7a9cdcedb2a9648dd1e")

	depends_on("r@2.5:", type=("build", "run"))

	# experiment