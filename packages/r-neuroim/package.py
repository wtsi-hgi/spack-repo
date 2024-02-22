# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeuroim(RPackage):
	"""Data Structures and Handling for Neuroimaging Data

	A collection of data structures that represent
    volumetric brain imaging data. The focus is on basic data handling for 3D
    and 4D neuroimaging data. In addition, there are function to read and write
    NIFTI files and limited support for reading AFNI files.
	"""
	
	cran = "neuroim" 

	version("0.0.6", md5="c8a8906d64e36c460e2eccd581eefa98")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-yaimpute", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
