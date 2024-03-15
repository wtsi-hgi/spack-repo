# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDicomread(RPackage):
	"""Reading and Saving DICOM Image Files

	This function provides an interface between 'Matlab' and 'R' in facilitating fast processing for reading and saving DICOM images.
	"""
	
	cran = "DICOMread" 

	version("0.0.0.3", md5="fe38d6712448c438f82869bb146cdc39")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matlabr", type=("build", "run"))
