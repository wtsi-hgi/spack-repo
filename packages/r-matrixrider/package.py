# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixrider(RPackage):
	"""Obtain total affinity and occupancies for binding site matrices on a given sequence

	Calculates a single number for a whole sequence that reflects the propensity of a DNA binding protein to interact with it. The DNA binding protein has to be described with a PFM matrix, for example gotten from Jaspar.
	"""
	
	bioc = "MatrixRider" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MatrixRider_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MatrixRider/MatrixRider_1.34.0.tar.gz"]

	version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="43461e624d1375b0fc7102955ef4d18b8a4568a5a23f02d79000ccfd47303f08")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-tfbstools", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
