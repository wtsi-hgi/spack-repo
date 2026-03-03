# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHandtill2001(RPackage):
	"""Multiple Class Area under ROC Curve

	An S4 implementation of Eq. (3) and Eq. (7) by
    David J. Hand and Robert J. Till (2001) <DOI:10.1023/A:1010920819831>.
	"""
	
	homepage = "https://gitlab.com/fvafrCU/HandTill2001"
	cran = "HandTill2001" 

	version("1.0.1", md5="e49c128276bf5e86eb9bf487113812aa", url="https://cran.r-project.org/src/contrib/HandTill2001_1.0.1.tar.gz")

	depends_on("r@2.14:", type=("build", "run"))
