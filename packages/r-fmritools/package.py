# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmritools(RPackage):
	"""Routines for Common fMRI Processing Tasks

	Supports fMRI (functional magnetic resonance imaging) 
    analysis tasks including reading in 'CIFTI', 'GIFTI' and 
    'NIFTI' data, temporal filtering, nuisance regression, and 
    aCompCor (anatomical Components Correction) (Muschelli et al.
    (2014) <doi:10.1016/j.neuroimage.2014.03.028>).
	"""
	
	homepage = "https://github.com/mandymejia/fMRItools"
	cran = "fMRItools" 

	version("0.4.2", md5="8e3004390447df2fad4040bbee49e780")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
