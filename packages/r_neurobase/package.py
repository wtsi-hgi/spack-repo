# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeurobase(RPackage):
	"""'Neuroconductor' Base Package with Helper Functions for 'nifti'
Objects

	Base package for 'Neuroconductor', which includes many helper 
    functions that interact with objects of class 'nifti', implemented by
    package 'oro.nifti', for reading/writing and also other manipulation 
    functions.
	"""
	
	cran = "neurobase" 

	version("1.32.3", md5="87a084afc63f70c758d24223ba15575a")

	depends_on("r-oro-nifti@0.11.3:", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
