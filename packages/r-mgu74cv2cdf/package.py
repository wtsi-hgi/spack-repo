# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74cv2cdf(RPackage):
	"""mgu74cv2cdf

	A package containing an environment representing the MG_U74Cv2.CDF file.
	"""
	
	bioc = "mgu74cv2cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74cv2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74cv2cdf/mgu74cv2cdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="2207a717b0864c29a99e521951b2dc83a611aba05509388d66a347eea09a61a2")

	depends_on("r-annotationdbi", type=("build", "run"))

