# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROroDicom(RPackage):
	"""Rigorous - DICOM Input / Output

	Data input/output functions for data that conform to the
    Digital Imaging and Communications in Medicine (DICOM) standard, part
    of the Rigorous Analytics bundle.
	"""
	
	homepage = "http://rig.oro.us.com"
	cran = "oro.dicom" 

	version("0.5.3", md5="c46d214d446f34b25ba5ca415ccf7d3b")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-oro-nifti@0.4:", type=("build", "run"))
