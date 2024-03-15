# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFslr(RPackage):
	"""Wrapper Functions for 'FSL' ('FMRIB' Software Library) from
Functional MRI of the Brain ('FMRIB')

	Wrapper functions that interface with 'FSL' 
    <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/>, a powerful and commonly-used 'neuroimaging'
    software, using system commands. The goal is to be able to interface with 'FSL'
    completely in R, where you pass R objects of class 'nifti', implemented by
    package 'oro.nifti', and the function executes an 'FSL' command and returns an R
    object of class 'nifti' if desired.
	"""
	
	cran = "fslr" 

	version("2.25.2", md5="f6103b1301d034c0d01deaf47f8359d4")

	depends_on("r-oro-nifti@0.5:", type=("build", "run"))
	depends_on("r-neurobase@1.32:", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("fsl", type=("build", "link", "run"))
