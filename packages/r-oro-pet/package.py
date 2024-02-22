# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROroPet(RPackage):
	"""Rigorous - Positron Emission Tomography

	Image analysis techniques for positron emission tomography
    (PET) that form part of the Rigorous Analytics bundle.
	"""
	
	homepage = "http://rig.oro.us.com"
	cran = "oro.pet" 

	version("0.2.7", md5="5603be66054e27f141be9a4b0f186345")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-oro-dicom@0.4:", type=("build", "run"))
	depends_on("r-oro-nifti@0.4:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
