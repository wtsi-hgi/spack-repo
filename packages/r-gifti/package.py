# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGifti(RPackage):
	"""Reads in 'Neuroimaging' 'GIFTI' Files with Geometry Information

	Functions to read in the geometry format under the 
    'Neuroimaging' 'Informatics' Technology Initiative ('NIfTI'), called 
    'GIFTI' <https://www.nitrc.org/projects/gifti/>. 
    These files contain surfaces of brain imaging data.
	"""
	
	cran = "gifti" 

	version("0.8.0", md5="c8be604c38997469aac54465615981de")

	depends_on("r-xml2@1.1.1:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
