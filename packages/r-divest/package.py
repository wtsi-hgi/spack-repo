# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDivest(RPackage):
	"""Get Images Out of DICOM Format Quickly

	Provides tools to sort DICOM-format medical image files, and
    convert them to NIfTI-1 format.
	"""
	
	homepage = "https://github.com/jonclayden/divest"
	cran = "divest" 

	version("1.0.0", md5="6f3902b4d8249698249d941083a094df")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
